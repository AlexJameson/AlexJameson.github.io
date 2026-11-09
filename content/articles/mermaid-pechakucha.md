+++
title = "Mermaid для технических писателей — печакуча-версия"
date = "2026-11-08"
description = "20 слайдов о том, почему Mermaid лучше PlantUML, какие диаграммы использовать в документации и как они помогают ИИ-агентам. Формат печакуча: читайте в своём темпе."
template = "slides.html"

[taxonomies]
tags = ["инструменты", "диаграммы", "docs-as-code"]
+++

## Диаграммы как код

Mermaid для технических писателей — в формате печакуча: 20 слайдов, каждый — одна мысль. Никакого автопереключения, листайте в своём темпе.

<!-- slide -->

## Проблема

Диаграммы нужны всем, но классический цикл «нарисовал в draw.io → экспортировал PNG → вставил в статью» убивает: картинки устаревают, не версионируются, а правка одного узла требует перегенерации всего изображения.

<!-- slide -->

## Решение

Mermaid превращает диаграмму в код: текст в Markdown, рендеринг в браузере. Диаграмма версионируется в git, диффается pull request'ами и живёт рядом с документацией, которую описывает.

<!-- slide -->

## Mermaid vs PlantUML: рендеринг

PlantUML требует Java-рантайма или серверной рендерилки. Mermaid — нативный JavaScript в браузере: один JS-файл, ноль инфраструктуры, работает с любым статическим генератором.

<!-- slide -->

## Mermaid vs PlantUML: экосистема

GitHub, GitLab, Notion и Obsidian поддерживают Mermaid из коробки. PlantUML — через плагины или никак. Синтаксис Mermaid компактнее и читается прямо в исходном Markdown. Для docs-as-code это решающее преимущество.

<!-- slide -->

## Flowchart: стратегии разрешения конфликтов

Самый универсальный тип диаграмм — flowchart. Алгоритмы, архитектурные схемы, пользовательские сценарии. Пример: как сервис синхронизации выбирает стратегию разрешения конфликтов.

{% mermaid() %}
flowchart TD
    A[Sync Process] --> B{Conflict Detected?}
    B -->|No| C[Apply Changes]
    B -->|Yes| D{Strategy}
    D -->|Manual| E[Queue for Review]
    D -->|Source Wins| F[Use Source Data]
    D -->|Target Wins| G[Use Target Data]
    D -->|Newest Wins| H[Compare Timestamps]
    E --> I[Manual Resolution]
    F --> C
    G --> C
    H --> C
    I --> C
{% end %}

<!-- slide -->

## Flowchart: архитектура сервиса

Тот же тип диаграмм для архитектуры: источники, API, целевые системы и обратная синхронизация.

{% mermaid() %}
graph LR
    A[Data Source] -->|Read| B[PinkCloudSync API]
    B -->|Write| C[Target System]
    C -->|Reverse Sync| B
    B -->|Update| A
    B -->|Detect Conflicts| D[Resolution Module]
    D -->|Apply Strategy| B
{% end %}

<!-- slide -->

## ELK layout для сложных схем

На больших схемах с подграфами дефолтный layout расползается. ELK распределяет узлы упорядоченно — разница заметна на диаграммах с десятком+ узлов.

{% mermaid(layout="elk") %}
flowchart TD
    subgraph Sources
        A[PostgreSQL]
        B[REST API]
        C[CSV Files]
    end
    subgraph Processing
        D[PinkCloudSync API]
        E[Sync Engine]
        F[Conflict Resolver]
    end
    subgraph Targets
        G[MySQL]
        H[MongoDB]
        I[Webhook]
    end
    A --> D
    B --> D
    C --> D
    D --> E
    E --> F
    E --> G
    E --> H
    E --> I
    F --> D
{% end %}

<!-- slide -->

## Sequence diagram: порядок вызовов

Когда важна последовательность, а не структура: кто кому и в каком порядке звонит. Классический сценарий — аутентификация через токен.

{% mermaid() %}
sequenceDiagram
    participant Client
    participant API
    Client->>API: POST /auth/token (api_key, api_secret)
    API->>Client: access_token (JWT)
    Client->>API: GET /sync/sessions (Authorization: Bearer token)
    API->>Client: Response data
{% end %}

<!-- slide -->

## Sequence: фишки

`autonumber` нумерует сообщения, `rect` выделяет фрагменты сценария, `note over` добавляет комментарии. Всё это читается прямо в исходном Markdown и не требует перерисовки.

<!-- slide -->

## State diagram: жизненный цикл объекта

Состояния и переходы: workflow публикации, CI/CD-пайплайны, обработка заказов. Пример — жизненный цикл сессии синхронизации.

{% mermaid() %}
stateDiagram-v2
    [*] --> pending: Create session
    pending --> in_progress: Start sync
    in_progress --> completed: Success
    in_progress --> failed: Error
    failed --> [*]
    completed --> [*]
{% end %}

<!-- slide -->

## Зачем нужен state diagram

Каждый переход помечен событием, которое его вызывает. Такая диаграмма сразу отвечает на вопрос: «Что может произойти дальше?» — лучше любого текстового описания.

<!-- slide -->

## ИИ-агенты: создание

Главное преимущество текстового формата: агенту не нужно генерировать бинарные файлы или координаты SVG. Достаточно выдать структурированный текст в синтаксисе Mermaid — задача, с которой LLM справляются надёжно.

<!-- slide -->

## ИИ-агенты: обновление

Правка одного узла или связи — это правка одной строки. Diff читается человеком и машиной одинаково легко, ревью диаграммы происходит в том же pull request, что и текст.

<!-- slide -->

## ИИ-агенты: извлечение

Диаграмму можно распарсить регулярными выражениями или простым скриптом — извлечь список компонентов, зависимостей или состояний. Диаграмма становится данными, а не картинкой.

{% mermaid() %}
graph LR
    A[Create Session] --> B[Data Reading]
    B --> C[Processing]
    C --> D{Conflicts?}
    D -->|Yes| E[Resolve]
    D -->|No| F[Write Data]
    E --> F
    F --> G[Complete]
{% end %}

<!-- slide -->

## Текст бьёт пиксели

Сравните с draw.io: там агент должен оперировать координатами пикселей или JSON-схемой. На порядок сложнее, хуже поддаётся контролю, а результат не ревьюится глазами без рендеринга.

<!-- slide -->

## Стилизация и темы

Встроенные темы: `default`, `dark`, `forest`, `neutral`, `base`. Последняя позволяет полностью переопределить цвета через `themeVariables`. Вывод — SVG: масштабируется без потерь на любых экранах и стилизуется через CSS.

<!-- slide -->

## Чеклист: какую диаграмму выбрать

Архитектура или алгоритм → flowchart. Сложная схема → flowchart + ELK. Вызовы API → sequence. Жизненный цикл → state. Структура данных → class. Доли и пропорции → pie. Динамика во времени → XY chart.

<!-- slide -->

## Что ещё уметь

Кликабельные узлы (`click A href "/api-reference"`), нативный рендеринг в GitHub README/issues/PR, accessibility через заголовки SVG, расширения для VS Code, Obsidian, Notion, Confluence.

<!-- slide -->

## С чего начать

[Mermaid Live Editor](https://mermaid.live/) — эксперименты с синтаксисом в реальном времени, без установки чего-либо. Mermaid — не просто замена PlantUML, а инструмент под современный docs-as-code: браузер, git, GitHub и ИИ-агенты из коробки.
