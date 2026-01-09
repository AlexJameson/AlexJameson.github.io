+++
title = "Zensical, новый SSG от создателей Material for MkDocs"
date = "2026-09-01"
description = "Первый взгляд на новый генератор от создателей одного из самых популярных инструментов."

[taxonomies]
tags=["инструменты"]
+++

## TL;DR

Я подготовил пример документации с помощью Zensical: [PinkCloudSync Docs](https://alexjameson.sourcecraft.site/pink-sync-docs/). В этом проекте я проверил основную функциональность и остался в целом доволен. Сам сайт я разместил на платформе [SourceCraft](https://sourcecraft.dev/) с помощью аналога GitHub Pages. Исходники документации можно посмотреть в [репозитории](https://sourcecraft.dev/alexjameson/pink-sync-docs).

Что мне понравилось:

* Простая конфигурация, быстрый запуск с нуля;
* Современный внешний вид и UX;
* Много продвинутых возможностей с нативной поддержкой вроде комментариев, тегов и аналитики;
* Поддержка множества плагинов и расширений из экосистемы MkDocs.

Главный минус в том, что проект только развивается и еще не достиг паритета по функциональности с MkDocs. Фактически, сейчас закончена работа над основами новой архитектуры, а функциональность из плагинов и расширений позволяет делать то же самое, что и в самом MkDocs.

![pinkcloudsync docs main page](/assets/pinkcloudsync-main.png)

## Обзор

[Zensical](https://zensical.org/) — это современный генератор статических сайтов для технической документации, разработанный командой, стоящей за популярной темой Material for MkDocs. О создании нового инструмента было объявлено 5 ноября в [блоге Material for MkDocs](https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/). До этого Material for MkDocs не получал обновлений более года.

Название Zensical (я его понимаю как *Zen* + суффикс *ical* как в logical) отражает философию инструмента: достижение дзена в процессе создания документации. К сожалению, узнать о достижение дзена с территории России нельзя, поэтому для доступа к сайту нужно применить технические меры.

Прежде всего — зачем нужно было с нуля переписывать настолько популярный инструмент? Пост авторов даёт ответ: c 2016 года накопилось слишком много устаревших вещей, которые не давали проекту идти в ногу со временем. Большая часть работы, законченной к настоящему моменту (январь 2026), относится к планированию переработки ключевых концепций. Подробнее можно узнать на странице [Compatibility](https://zensical.org/compatibility/).

Например, для сборки документации используется написанный с нуля на Rust движок [ZRX](https://github.com/zensical/zrx/). Он сам по себе является отдельным опенсорсным проектом. При этом Zensical распространяется как пакет в экосистеме Python. Заявлено как минимум пятикратное превосходство в скорости сборки и отсуствие проблем со сборкой больших проектов.

Вместе со сборщиком для проекта написан на Rust новый сервер для локальной сборки, заменяющий обычный [Python HTTPServer](@/articles/web-server.md), использующийся в MkDocs.

Также разработчики готовят к выкладке в опенсорс их новый поиск — Disco, который уже сейчас работает в Zensical. Я его протестировал, но у меня слишком маленький проект, чтобы полностью оценить его возможности. В целом — очень достойно.

### Диалект Markdown

Zensical использует популярный диалект [Python-Markdown](https://python-markdown.github.io/), что обеспечивает совместимость со стандартным синтаксисом CommonMark, но значительно [расширяет его](https://zensical.org/docs/authoring/markdown/).

Из коробки поддерживаются все фичи [GitHub Flavored Markdown (GFM)](https://github.github.com/gfm/), а дополнительная функциональность вроде вкладок и диаграмм реализуется с помощью [PyMdown Extensions](https://zensical.org/docs/setup/extensions/python-markdown-extensions/).

### Какие возможности поддержаны сейчас

Zensical уже сейчас предлагает мощный набор функций для конфигурации сайта, не требующих сложной настройки.

1. **Навигация**: Автоматическая генерация меню, поддержка вложенных разделов и хлебных крошек.
1. **Поиск**: Быстрый полнотекстовый поиск с подсветкой результатов (настраивается через `search.highlight`).
1. **Система комментариев** (интересно, можно ли её приспособить для ревью собранной документации).
1. **Кастомизация внешнего вида**: Гибкая система тем, настройка хедера и футера. В моём примере используется тема с розовым акцентом:

    ```toml
    [[project.theme.palette]]
    primary = "pink"
    accent = "purple"
    ```

Полный список возможностей см. в [документации](https://zensical.org/docs/setup/basics/).

Отдельно можно посмотреть на [список элементов](https://zensical.org/docs/authoring/markdown/), которые расширяют обычный Markdown. Есть поддержка множества элементов, включая таблицы, сноски, разные виды списков, тултипы и т.д.

## Планы по развитию

Zensical — это активно развивающийся проект. Согласно [роадмапу](https://zensical.org/about/roadmap/), можно ожидать следующего в 2026 году:

* **Модульная система**: Переход к архитектуре, которая позволит еще проще создавать и подключать расширения. 
* **Система компонентов**: Возможность создавать переиспользуемые UI-компоненты для документации, что приблизит Zensical к современным фреймворкам для веб-разработки. Если я правильно понимаю идею, то это аналог [MDX](https://mdxjs.com/). Также заслуживает внимание желание отказаться в принципе от сочетания PyMdown и Jinja2 в пользу [системы компонентов](https://zensical.org/about/roadmap/#component-system), но приоритет команды сейчас — это поддержка полной совместимости с MkDocs.
* **Инструменты для API-документации**: Это, пожалуй, самая ожидаемая лично мной часть. Сейчас поддержка API-документации ограничена (в основном через [mkdocstrings](https://zensical.org/docs/setup/extensions/mkdocstrings/)), и очень не хватает специализированных плагинов, аналогичных тем, что есть в экосистеме MkDocs. Разработчики обещают представить поддержку генерации документации из коробки, да еще и с продвинутыми возможностями, например чтобы встраивать 

Прежде всего я бы выделил отказ от монолитной архитектуры и переход на более гибкую [модульную](https://zensical.org/about/roadmap/#module-system). 

### MkDocs и Zensical

Одной из особенностей Zensical является использование формата [TOML](https://toml.io/en/) для конфигурации вместо **YAML**, привычного пользователям MkDocs. Но различие в форматах не нарушает обратной совместимости, миграцию базовой функциональности обещают без проблем.

**TOML** (Tom's Obvious, Minimal Language) был выбран не случайно. В отличие от YAML, который часто критикуют за неоднозначность парсинга и проблемы с отступами, TOML предлагает:

* **Отсутствие проблем с отступами**: Структура определяется явными секциями `[section]`, а не пробелами.
* **Читаемость для сложных конфигураций**: Вложенные настройки плагинов и расширений выглядят понятнее.
* **Строгую типизацию**: Числа, строки, даты и булевы значения четко определены.

#### Соответствие mkdocs.yml и zensical.toml

Переход с MkDocs на Zensical интуитивно понятен, так как структура конфигурации очень похожа.

**MkDocs (YAML):**

```yaml
site_name: My Docs
nav:
  - Home: index.md
theme:
  name: material
  features:
    - navigation.tabs
markdown_extensions:
  - admonition
```

**Zensical (TOML):**

```toml
[project]
site_name = "My Docs"

nav = [
  { "Home" = "index.md" }
]

[project.theme]
features = [
    "navigation.tabs"
]

markdown_extensions = [
    "admonition"
]
```

## Работа с Zensical

[Начать работу](https://zensical.org/docs/get-started/) с Zensical очень просто. Процесс сводится к нескольким шагам:

1. **Установка**: `pip install zensical`. Я, конечно, рекомендую устанавливать все в виртуальном окружении, а в документации ещё есть модный способ установки через [uv](docs.astral.sh/uv/).
1. **Инициализация**: `zensical new .` для создания нового проекта в текущей директории. Появляется файл конфигурации `zensical.toml` в корне проекта, а также директория `docs/` с файлами `index.md` и `markdown.md`.
1. **Запуск**: `zensical serve` для локального просмотра с live-reload.

Инструмент спроектирован так, чтобы минимизировать время от установки до первого результата. При первом запуске мне не пришлось что-то кастомизировать или задавать тему — отличная тема уже встроена и настроена по умолчанию.

### Настройка первого сайта

Для начала имеет смысл определиться с тем, какую функциональность нужно подключить. Я хорошо представлял, какой должна быть документация в примере:

* Вкладки для разных языков;
* Диаграммы Mermaid;
* Сниппеты для переиспользования контента;
* Подсветка кода в примерах;
* Сноски, аббревиатуры и другие мелочи.

Вот какой у меня получился [файл конфигурации](https://sourcecraft.dev/alexjameson/pink-sync-docs/browse/zensical.toml). Вышеперечисленная функциональность настроена в блоке `markdown_extensions`:

```toml
# ============================================================================
# PinkCloudSync Documentation Configuration
# ============================================================================

[project]

# The site_name is shown in the page header and the browser window title
site_name = "PinkCloudSync Docs"

# The site_description is included in the HTML head
site_description = "Documentation for PinkCloudSync — an interface for data synchronization between systems"

# The site_author attribute
site_author = "PinkCloudSync Team"

# The copyright notice appears in the page footer
copyright = """
Copyright &copy; 2025 PinkCloudSync Team
"""

# Navigation structure
nav = [
  { "Home" = "index.md" },
  { "Getting Started" = "getting-started.md" },
  { "Concepts" = [
    { "Overview" = "concepts/overview.md" },
  ]},
  { "Guides" = [
    { "Authentication" = "guides/authentication.md" },
    { "Data Synchronization" = "guides/data-sync.md" },
    { "Conflict Resolution" = "guides/conflict-resolution.md" },
  ]},
]

# Markdown Extensions
markdown_extensions = [
    "admonition",
    "footnotes",
    "pymdownx.snippets",
    { "pymdownx.superfences" = { custom_fences = [{ name = "mermaid", class = "mermaid", format = "pymdownx.superfences.fence_code_format" }] } },
    { "pymdownx.tabbed" = { alternate_style = true } },
    "pymdownx.tasklist",
    { "pymdownx.highlight" = { linenums = true } },
    "pymdownx.inlinehilite",
    "pymdownx.details",
    "abbr",
]

# ----------------------------------------------------------------------------
# Theme configuration
# ----------------------------------------------------------------------------
[project.theme]

# Use English language = "en"

features = [
    "announce.dismiss",
    "content.code.annotate",
    "content.code.copy",
    "content.code.select",
    "content.footnote.tooltips",
    "content.tabs.link",
    "content.tooltips",
    "navigation.footer",
    "navigation.indexes",
    "navigation.instant",
    "navigation.instant.prefetch",
    "navigation.path",
    "navigation.sections",
    "navigation.top",
    "navigation.tracking",
    "search.highlight",
]

# Color schemes
[[project.theme.palette]]
scheme = "default"
primary = "pink"
accent = "purple"
toggle.icon = "lucide/sun"
toggle.name = "Switch to dark mode"

[[project.theme.palette]]
scheme = "slate"
primary = "pink"
accent = "purple"
toggle.icon = "lucide/moon"
toggle.name = "Switch to light mode"

# Fonts
[project.theme.font]
text = "Inter"
code = "JetBrains Mono"

# Icons
[project.theme.icon]
logo = "lucide/cloud-sync"

# ----------------------------------------------------------------------------
# Extra settings
# ----------------------------------------------------------------------------

# Enable Mermaid diagrams
[project.extra.mermaid]

[[project.extra.social]]
icon = "fontawesome/brands/github"

link = "https://github.com/pinkcloudsync/api"
```

### Настройка темы

В `[project.theme]` у меня указано много параметров, улучшающих внешний вид и UX. В `features` указаны

#### Переиспользование контента (Snippets)

В проекте используется мощная фича — сниппеты. В файле `docs/getting-started.md` мы видим:

```markdown
--8<-- "docs/.snippets:2:9"
```

Это позволяет вставлять куски текста или кода из внешних файлов, что идеально для поддержки актуальности примеров кода, которые могут тестироваться отдельно.
