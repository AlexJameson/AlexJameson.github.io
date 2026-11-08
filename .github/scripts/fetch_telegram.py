#!/usr/bin/env python3
"""Fetch Telegram channel posts from the public t.me/s preview and write them
as Zola pages. Runs in GitHub Actions before the build; commits are handled
by the workflow.

Stdlib-only on purpose: no pip installs in CI.

Environment:
    TELEGRAM_CHANNEL   channel username without @ (required)
    TELEGRAM_LIMIT     how many recent posts to keep in sync (default 30)
"""

import html
import json
import os
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT_DIR = ROOT / "content" / "telegram"
IMG_DIR = ROOT / "static" / "telegram" / "img"
STATE_FILE = ROOT / ".github" / "scripts" / ".telegram_state.json"

ALLOWED_TAGS = {"b", "strong", "i", "em", "u", "s", "a", "br", "code", "pre", "blockquote"}
MAX_PHOTOS_PER_POST = 4
USER_AGENT = "Mozilla/5.0 (compatible; site-feed-bot/1.0)"


class MessageExtractor(HTMLParser):
    """Pull messages out of the t.me/s server-rendered preview in one pass.

    Structure per message:
        <div class="... tgme_widget_message" data-post="channel/123">
          ...
          <div class="tgme_widget_message_text" dir="auto"> ... post html ... </div>
          <a class="tgme_widget_message_photo_wrap" style="background-image:url('...')">
          ...
          <time datetime="...">
        </div>
    """

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.messages = []
        self._msg_depth = 0
        self._text_depth = 0
        self._in_text = False
        self._text_sanitizer = None

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag == "div" and attr.get("data-post", "").count("/") == 1:
            self.messages.append(
                {
                    "id": attr["data-post"].split("/")[-1],
                    "date": None,
                    "text": "",
                    "photos": [],
                }
            )
            self._msg_depth = 1
            return
        if not self.messages:
            return
        if self._msg_depth and tag == "div":
            self._msg_depth += 1
        if self._in_text:
            self._text_depth += 1
            self._text_sanitizer.handle_starttag(tag, attrs)
            return
        msg = self.messages[-1]
        if tag == "div" and attr.get("class", "").startswith("tgme_widget_message_text"):
            self._in_text = True
            self._text_depth = 1
            self._text_sanitizer = TextSanitizer()
            return
        if tag == "time" and attr.get("datetime") and not msg["date"]:
            msg["date"] = attr["datetime"]
        if tag == "a" and "tgme_widget_message_photo_wrap" in attr.get("class", ""):
            style = attr.get("style", "")
            m = re.search(r"background-image:url\('([^']+)'\)", style)
            if m and len(msg["photos"]) < MAX_PHOTOS_PER_POST:
                msg["photos"].append(html.unescape(m.group(1)))

    def handle_startendtag(self, tag, attrs):
        if self._in_text:
            self._text_sanitizer.handle_startendtag(tag, attrs)

    def handle_endtag(self, tag):
        if not self.messages:
            return
        if self._in_text:
            self._text_depth -= 1
            if self._text_depth == 0:
                self._in_text = False
                self.messages[-1]["text"] = "".join(self._text_sanitizer.out).strip()
                self._text_sanitizer = None
            else:
                self._text_sanitizer.handle_endtag(tag)
            return
        if self._msg_depth and tag == "div":
            self._msg_depth -= 1

    def handle_data(self, data):
        if self._in_text:
            self._text_sanitizer.handle_data(data)


class TextSanitizer(HTMLParser):
    """Rebuild message HTML keeping only ALLOWED_TAGS, keeping link text."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in ALLOWED_TAGS:
            return
        if tag == "a":
            href = dict(attrs).get("href", "")
            if not href.startswith(("http://", "https://")):
                return
            self.out.append(f'<a href="{html.escape(href, quote=True)}" rel="noopener">')
        else:
            self.out.append(f"<{tag}>")
        self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        if tag == "br":
            self.out.append("<br>")

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.out.append(f"</{tag}>")
            self.stack.pop()

    def handle_data(self, data):
        self.out.append(html.escape(data))


def extract_texts(raw_html, messages):  # kept for tests
    return {m["id"]: m["text"] for m in messages}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"fetched": []}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def toml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def plain_text(html_text):
    text = re.sub(r"<br\s*/?>", " ", html_text)
    text = re.sub(r"</(p|div|blockquote|li)>", " ", text)
    return re.sub(r"<[^>]+>", "", text).strip()


def download_photo(url, path):
    if path.exists():
        return
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        if len(data) > 1024:  # basic sanity check
            path.write_bytes(data)
    except Exception as e:  # noqa: BLE001 - feed must not break the build
        print(f"warn: photo download failed {url}: {e}", file=sys.stderr)


def write_post(msg, channel):
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    msg_id = msg["id"]
    text_html = msg["text"]
    plain = plain_text(text_html)
    title = plain[:60].rsplit(" ", 1)[0] + ("…" if len(plain) > 60 else "") if plain else f"Пост {msg_id}"

    photo_html = ""
    for i, url in enumerate(msg["photos"]):
        ext = ".jpg"
        m = re.search(r"\.(jpe?g|png|webp)", url.split("?")[0], re.I)
        if m:
            ext = m.group(0).lower().replace("jpeg", ".jpg") if m.group(0).lower() == ".jpeg" else m.group(0).lower()
        fname = f"{msg_id}-{i}{ext}"
        download_photo(url, IMG_DIR / fname)
        photo_html += f'\n<img src="/telegram/img/{fname}" alt="" loading="lazy">\n'

    tg_url = f"https://t.me/{channel}/{msg_id}"
    body = (text_html + "\n" + photo_html).strip()
    if not body:
        body = "<p><em>(медиа-пост — смотрите оригинал)</em></p>"

    fm = f"""+++
title = {toml_str(title)}
date = {toml_str(msg['date'])}
description = {toml_str(plain[:150])}

[taxonomies]
tags = ["telegram"]

[extra]
tg_id = {msg_id}
tg_url = {toml_str(tg_url)}
+++

{body}
"""
    (CONTENT_DIR / f"{msg_id}.md").write_text(fm, encoding="utf-8")


def sync_page(channel, before=None):
    url = f"https://t.me/s/{channel}" + (f"?before={before}" if before else "")
    raw = fetch(url)
    extractor = MessageExtractor()
    extractor.feed(raw)
    return extractor.messages


SKIP_TAG = os.environ.get("TELEGRAM_SKIP_TAG", "#noarchive")
# Short posts whose main payload is a link to our own site (article
# announcements, "read on the site" funnels) are noise in the on-site archive:
# the destination content already lives here. Configurable, off if empty.
OWN_DOMAIN = os.environ.get("TELEGRAM_OWN_DOMAIN", "alexjameson.github.io")
# below this text length a post linking to OWN_DOMAIN is treated as an announcement
ANNOUNCE_MAX_LEN = 400


def is_excluded(text_html, plain):
    if SKIP_TAG and SKIP_TAG.lower() in plain.lower():
        return True
    if OWN_DOMAIN and OWN_DOMAIN in text_html and len(plain) <= ANNOUNCE_MAX_LEN:
        return True
    return False


def main():
    channel = os.environ.get("TELEGRAM_CHANNEL", "").lstrip("@")
    if not channel:
        sys.exit("TELEGRAM_CHANNEL env var is required")
    limit = int(os.environ.get("TELEGRAM_LIMIT", "30"))

    # t.me/s renders messages oldest-first within the visible window;
    # ?before=<id> pages to older messages.
    messages = sync_page(channel)
    if not messages:
        print("no messages found; is the channel public?", file=sys.stderr)
        return

    while len(messages) < limit:
        oldest = messages[0]["id"]
        older = sync_page(channel, before=oldest)
        if not older or older[-1]["id"] == messages[0]["id"]:
            break
        messages = older + messages
        time.sleep(1)

    messages = messages[-limit:]

    keep = {m["id"] for m in messages}
    for f in CONTENT_DIR.glob("*.md"):
        if f.stem != "_index" and f.stem not in keep:
            f.unlink()

    synced = 0
    skipped = 0
    for msg in messages:
        if is_excluded(msg["text"], plain_text(msg["text"])):
            stale = CONTENT_DIR / f"{msg['id']}.md"
            if stale.exists():
                stale.unlink()  # tag added after an earlier sync
            skipped += 1
            continue
        write_post(msg, channel)
        synced += 1

    state = load_state()
    state["fetched"] = [m["id"] for m in messages]
    state["channel"] = channel
    save_state(state)
    print(f"synced {synced} posts from {channel} ({skipped} excluded)")


if __name__ == "__main__":
    main()
