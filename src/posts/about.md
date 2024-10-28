---
title: Обо мне
description: Кто я, чем занимаюсь и чем могу быть полезен
tags:
  - personal
---

Nulite is a simple, elegant, minimalistic stater project for [Eleventy](https://www.11ty.dev/) to help you create a simple blog with focus on performance and simplicity.

This project is strongly influenced by [Steph Ango's blog](https://stephango.com/) (one of the creators of Obsidian).

If you like the project feel free to leave a star ⭐ You can also send me issues that you can find or proposals for improvement in PRs.

This project is under the domain of [CodingPotions, a Spanish programming blog](https://codingpotions.com).

## Features

- 🧐 Simple. Elegant, minimalist design, clear and easy to read.
- 📈 Good performance. Inline styles and the minimum amount of JS to make the page load as fast as possible.
- 🌙 Support for light/dark mode. Respects user tastes and allows toggle between both saving preferences.
- 📡 RSS. Bring back old days.
- 🎨 Easily customizable. Thanks to the CSS variables system you can change colors and fonts in one place.
- 🖍️ Syntax coloring. If you write blocks of code in the articles you will have coloring, and without adding extra JS.
- 📝 Article recommendation. Each article has a tag-based recommendation system to give the user more content to read.

## Getting started

1. Clone or fork this repo: `https://github.com/codingpotions/nulite`
2. `cd` into the project directory and run `npm install`

## Running and serving a dev build

```sh
npm run start
```

Browse to [http://localhost:8080](http://localhost:8080).

## Running and serving a prod build

```sh
npm run build
```

Output files are generated into the `_site` folder.

## Project structure

```
src/
  _includes/
    All UI partials. Inside the css folder, in the global.liquid you can change the CSS variables
  _data/
    Here you can change the site info, like the title and description
  posts/
    Each individual post in markdown files
  public/
    This folder contians statics files, copied directly into the output, like the favicon, for ecample
Configuration and build files
```
