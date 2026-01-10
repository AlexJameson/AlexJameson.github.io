+++
title = "Zensical, новый SSG от создателей Material for MkDocs"
date = "2026-01-10"
description = "Первый взгляд на новый генератор от создателей одного из самых популярных инструментов."

[taxonomies]
tags=["инструменты"]
+++

## TL;DR {#tldr}

Я подготовил пример документации с помощью Zensical: [PinkCloudSync Docs](https://alexjameson.sourcecraft.site/pink-sync-docs/). В этом проекте я проверил основную функциональность и остался в целом доволен. 

Сам сайт я разместил на платформе [SourceCraft](https://sourcecraft.dev/) с помощью аналога GitHub Pages. Исходники документации можно посмотреть в [репозитории](https://sourcecraft.dev/alexjameson/pink-sync-docs). SourceCraft я использовал из-за того, что GitHub Pages у меня уже занят, а проверить нашу платформу мне давно хотелось.

Что мне понравилось:

* Простая конфигурация, быстрый запуск с нуля;
* Современный внешний вид и UX;
* Много продвинутых возможностей с нативной поддержкой вроде комментариев, тегов и аналитики;
* Поддержка множества плагинов и расширений из экосистемы MkDocs.

Главный минус в том, что проект только развивается и еще не достиг паритета по возможностям с MkDocs. Сейчас завершена работа над основами новой архитектуры, а в будущем ожидается больше оригинальных решений.

![pinkcloudsync docs main page](/assets/pinkcloudsync-main.png)

## Обзор {#overview}

[Zensical](https://zensical.org/) — это современный генератор статических сайтов для технической документации, разработанный командой, стоящей за популярной темой Material for MkDocs. О создании нового инструмента было объявлено 5 ноября 2025 года в [блоге Material for MkDocs](https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/). До этого Material for MkDocs не получал обновлений более года.

Название Zensical (я его понимаю как *Zen* + суффикс *ical* как в logical) отражает философию инструмента: достижение дзена в процессе создания документации. К сожалению, узнать о достижение дзена с территории России нельзя, поэтому для доступа к сайту нужно применить технические меры.

Прежде всего — зачем нужно было с нуля переписывать настолько популярный инструмент? Пост авторов даёт ответ: c 2016 года накопилось слишком много устаревших вещей, которые не давали проекту идти в ногу со временем. Большая часть работы, законченной к настоящему моменту (январь 2026), относится к планированию переработки ключевых концепций. Подробнее можно узнать на странице [Compatibility](https://zensical.org/compatibility/).

Например, для сборки документации используется написанный с нуля на Rust движок [ZRX](https://github.com/zensical/zrx/). Он сам по себе является отдельным опенсорсным проектом. При этом Zensical распространяется как пакет в экосистеме Python. Заявлено как минимум пятикратное превосходство в скорости сборки и отсуствие проблем со сборкой больших проектов.

Вместе со сборщиком для проекта написан на Rust новый сервер для локальной разработки, заменяющий обычный [Python HTTP-сервер](@/articles/web-server.md), использующийся в MkDocs.

Также разработчики готовят к выкладке в опенсорс их новый поиск — Disco, который уже сейчас работает в Zensical. Я его протестировал, но у меня слишком маленький проект, чтобы полностью оценить его возможности. В целом — очень достойно.

### Диалект Markdown

Zensical использует популярный диалект [Python-Markdown](https://python-markdown.github.io/), что обеспечивает совместимость со стандартным синтаксисом CommonMark, но значительно [расширяет его](https://zensical.org/docs/authoring/markdown/).

Из коробки поддерживаются все фичи [GitHub Flavored Markdown (GFM)](https://github.github.com/gfm/), а дополнительная функциональность вроде вкладок и диаграмм реализуется с помощью [PyMdown Extensions](https://zensical.org/docs/setup/extensions/python-markdown-extensions/).

### Какие возможности поддержаны сейчас

Zensical уже сейчас предлагает мощный набор функций для конфигурации сайта, не требующих сложной настройки.

1. **Навигация**: Автоматическая генерация меню, поддержка вложенных разделов и хлебных крошек.
1. **Поиск**: Быстрый полнотекстовый поиск с подсветкой результатов (включен по умолчанию, настраивается через `search.highlight`).
1. **Система комментариев** (интересно, можно ли её приспособить для ревью собранной документации).
1. **Кастомизация внешнего вида**: Гибкая система тем, настройка хедера и футера. В моём примере используется тема с розовым акцентом:

    ```toml
    [[project.theme.palette]]
    primary = "pink"
    accent = "purple"
    ```

Полный список возможностей см. в [документации](https://zensical.org/docs/setup/basics/).

Отдельно можно посмотреть на [список элементов](https://zensical.org/docs/authoring/markdown/), которые расширяют обычный Markdown. Есть поддержка множества элементов, включая таблицы, сноски, разные виды списков, тултипы и т.д.

### Планы по развитию {#roadmap}

Zensical — это активно развивающийся проект. Согласно [роадмапу](https://zensical.org/about/roadmap/), можно ожидать следующего в 2026 году:

* **Модульная система**: Переход к архитектуре, которая изолирует ядро ZRX от дополнительной функциональности и позволит проще создавать и подключать расширения.
* **Система компонентов**: Возможность создавать переиспользуемые компоненты для документации, что приблизит Zensical к современным фреймворкам для веб-разработки. Если я правильно понимаю идею, то это аналог [MDX](https://mdxjs.com/). Также заслуживает внимание желание отказаться в принципе от сочетания PyMdown и Jinja2 в пользу [системы компонентов](https://zensical.org/about/roadmap/#component-system), но приоритет команды сейчас — это поддержка полной совместимости с MkDocs.
* **Инструменты для API-документации**: Это, пожалуй, самая ожидаемая лично мной часть. Сейчас поддержка API-документации ограничена (в основном через [mkdocstrings](https://zensical.org/docs/setup/extensions/mkdocstrings/)), и можно использовать только плагины из экосистемы MkDocs. Разработчики обещают представить поддержку генерации документации из коробки, да еще и с продвинутыми возможностями, например чтобы встраивать примеры кода.

### MkDocs и Zensical

Одной из особенностей Zensical является использование формата [TOML](https://toml.io/en/) для конфигурации вместо **YAML**, привычного пользователям MkDocs. Но различие в форматах не нарушает обратной совместимости, миграцию базовой функциональности обещают без проблем. Более того, в данный момент для обратной совместимости можно указать всю конфигурацию Zensical в `mkdocs.yml`.

**TOML** (Tom's Obvious, Minimal Language) был выбран не случайно. В отличие от YAML, который часто критикуют за неоднозначность парсинга и проблемы с отступами, TOML предлагает:

* **Отсутствие проблем с отступами**: Структура определяется явными секциями `[section]`, а не отступами.
* **Читаемость для сложных конфигураций**: Вложенные настройки плагинов и расширений выглядят понятнее.

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

markdown_extensions = [
    "admonition"
]

[project.theme]
features = [
    "navigation.tabs"
]
```

## Мой опыт работы с Zensical {#getting-started}

> Посмотреть на работающий сайт можно по следующему адресу: [PinkCloudSync Docs](https://alexjameson.sourcecraft.site/pink-sync-docs/).
> 
> Исходники я выложил на SourceCraft: [alexjameson/pink-sync-docs](https://sourcecraft.dev/alexjameson/pink-sync-docs).

[Начать работу](https://zensical.org/docs/get-started/) с Zensical очень просто. Процесс сводится к нескольким шагам в минималистичном [CLI](https://zensical.org/docs/usage/cli/):

1. **Установка**:
   Я рекомендую создать [виртуальное окружение](https://docs.python.org/3/library/venv.html) и установить пакеты в нём:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install zensical
   ```

   Можно выполнить и глобальную установку — `pip install zensical`, но это потенциально приводит к конфликтам с версиями пакетов.

   В документации также показан современный способ установки через [uv](docs.astral.sh/uv/).

1. **Инициализация**:
   `zensical new .` для создания нового проекта в текущей директории. 
   После выполнения команды появляется файл конфигурации `zensical.toml` в корне проекта, а также директория `docs/` с файлами `index.md` и `markdown.md`.

1. **Запуск**:
   `zensical serve` для локального просмотра с live-reload.

Инструмент спроектирован так, чтобы минимизировать время от установки до первого результата. При первом запуске мне не пришлось что-то кастомизировать или задавать тему — всё необходимое уже настроено по умолчанию.

После создания проекта имеет смысл определиться с тем, какую функциональность нужно подключить. Подробную информацию о возможностях можно найти в документации:

* [Basics](https://zensical.org/docs/setup/basics/)
* [Authoring](https://zensical.org/docs/authoring/markdown/)
* [Customization](https://zensical.org/docs/customization/)

### Настройка {#configuration}

Я хорошо представлял, какая функциональность должна быть в моём примере:

* [Вкладки](https://zensical.org/docs/authoring/content-tabs/) для разных языков;
* Диаграммы [Mermaid](https://zensical.org/docs/authoring/diagrams/);
* [Сниппеты](https://zensical.org/docs/setup/extensions/python-markdown-extensions/#snippets) для переиспользования контента;
* [Сноски](https://zensical.org/docs/authoring/footnotes/), аббревиатуры и другие мелочи.

Получившийся файл конфигурации можно изучить [по ссылке](https://sourcecraft.dev/alexjameson/pink-sync-docs/browse/zensical.toml).

Расширения указываются в блоке `markdown_extensions` в секции `[project]`:

```toml
[project]

# ...

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

# ...
```

Не дошли руки до тестирования [карточек (grids)](https://zensical.org/docs/authoring/grids/), [комментариев](https://zensical.org/docs/setup/comment-system/) и поддержки [разных языков](https://zensical.org/docs/setup/language/).

### Настройка темы {#theme-setup}

В блоке `[project.theme]` у меня указано много параметров, улучшающих внешний вид и UX.

В `features` у меня указаны способы кастомизировать поведение расширений. Такие способы приведены в документации (пример для [подсветки результатов поиска](https://zensical.org/docs/setup/search#search-highlighting)).

```toml
[project]

# ...

[project.theme]

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

# ...
```

В том же блоке `[project.theme]` я настроил шрифты, иконки и палитру темы сайта. Подробнее можно узнать в документации: [Colors](https://zensical.org/docs/setup/colors/), [Fonts](https://zensical.org/docs/setup/fonts/) и т.д.

```toml
[project]

# ...

[project.theme]

# ...

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
```

### Генерация справочника из OpenAPI {#openapi-reference}

Для генерации справочника из OpenAPI я использовал [MkDocs Swagger UI Tag](https://github.com/blueswen/mkdocs-swagger-ui-tag). Этот плагин хорошо знаком пользователям MkDocs. Он позволяет встроить в HTML полноценный Swagger UI и при желании настроить отображение справочника в `mkdocs.yml` или `zensical.toml`.

Чтобы включить генерацию, нужно добавить `[plugins.swagger-ui-tag]`, а также `extra_files` для добавления файла `openapi.yaml` в сборку:

```toml
[project]

# ...

# Plugins
[plugins.swagger-ui-tag]

extra_files = [
  "docs/openapi.yaml"
]

# ...
```

Посмотреть на сгенерированный справочник с поддержкой основной темы можно здесь: [API Reference](https://alexjameson.sourcecraft.site/pink-sync-docs/api-reference/).

### Переиспользование контента {#reuse-content}

Отдельно хочу поговорить про включение переиспользования контента. Для этой цели я использовал стандартное расширение [Snippets](https://zensical.org/docs/setup/extensions/python-markdown-extensions#snippets), с помощью которого указал в целевых файлах нужные диапазоны для включения из одного исходного файла.

В файле [docs/getting-started.md](https://sourcecraft.dev/alexjameson/pink-sync-docs/browse/docs/getting-started.md?rev=main&plain=true&l=9):

```markdown
# Getting Started

This guide will help you quickly get started with the PinkCloudSync service.

--8<-- "docs/.snippets:2:9"
```

Файл с исходниками для включения контента на этих строках выглядит так:

```markdown
;; prerequisites
## Prerequisites

Before you begin, make sure you have:

* An active PinkCloudSync account
* API key and secret (obtain from the [console](https://console.pinkcloudsync.example))
* Basic knowledge of REST APIs
* An installed tool for working with APIs (curl, Postman, or Python)
```

Получилось так:

![pinkcloudsync reuse content](/assets/pinkcloudsync-include.png)

### Выводы {#conclusion}

В общих чертах работа с Zensical напоминает работу с MkDocs + Material. Такой же быстрый старт, доступ к огромной экосистеме плагинов, но куда более современный UX и скорость работы модулей сборки и поиска. Однако нужно понимать, что полная совместимость с MkDocs — это временное состояние.

Сейчас еще рано делать выводы о том, каковы будут полные возможности инструмента, потому что в 2026 году ожидается переход на полноценную модульную систему, введение системы компонентов и переизобретение генерации API.

Я точно вернусь к проверке этого инструмента через некоторое время, потому что меня впечатляет гибкость и минималистичность настроек в сочетании с обещанием будущих возможностей. Чтобы не пропустить момент обновления, можно подписаться на [рассылку с обновлениями](https://zensical.org/about/newsletter/) Zensical и следить за их [роадмапом](https://zensical.org/about/roadmap/).
