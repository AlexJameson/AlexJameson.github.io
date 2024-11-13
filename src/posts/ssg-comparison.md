---
title: Сравнение генераторов статических сайтов для создания документации
description: Сравниваем шести генераторов статических сайтов (SSG) — Docusaurus, MkDocs, Diplodoc, Sphinx, Hugo и Jekyll.
tags:
  - инструменты
---

Цель сравнения — помочь людям, которые не слишком хорошо себе знакомы с различными генераторами статических сайтов, составить базовое представление о нескольких распространенных решениях. Обзор не претендует на объективность и показывает в первую очередь мой опыт.

Я сравнил генераторы по нескольким параметрам, которые кажутся мне достаточно важными и при этом доступными для анализа, но получившиеся результаты довольно субъективны. Причина в том, что я сам работаю в Яндексе и последние 4 года я пишу документацию с помощью Diplodoc. Это ведет к тому, что у меня самый актуальный и глубокий опыт именно с этим инструментом, а еще он мне просто нравится.

Результаты могут очень сильно различаться в зависимости от сценариев использования, для простоты я предполагаю, что мы сравниваем генераторы для небольшого документационного проекта объемом в пару десятков уже имеющихся Markdown-файлов. В этом обзоре не затронуты инструменты для AsciiDoc и других языков (за исключением Sphinx) так как у меня нет практического опыта работы с ними. Также я не рассмотрел самый популярный на GitHub генератор статических сайтов на основе Markdown под названием Gatsby, так как он давно стал фактически фреймворком для создания веб-приложений, а также потому, что я не следил за его развитием в последние годы и не ориентируюсь в существующих пяти версиях.

## Базовое сравнение

Можно выбрать любой из этих генераторов, все они обладают возможностями, которые позволяют делать удобные и кастомизируемые сайты. Везде сейчас есть поддержка диаграмм как кода, переиспользование контента, возможность встраивать генерацию по стандарту OpenAPI и многое другое.

Основные различия заключаются в наличии некоторых дополнительных возможностей, сложности конфигурации и эксплуатации.

### Tl;dr

* `Docusaurus` отлично подходит для любых проектов, позволяет добавить интерактивность и кастомизировать что угодно при знании React.
* `MkDocs` идеален для быстрого старта и простых проектов, широко распространен в индустрии.
* `Diplodoc` подходит для крупных и средних проектов, активно развивается. Единственный генератор в списке с изначально русскоязычным сообществом.
* `Sphinx` это сложный инструмент. Нужно быть готовым разбираться во множестве вещей, зато можно сделать практически что угодно.
* `Hugo` выделяется скоростью и производительностью, подойдет для самых разных проектов — от блогов до больших порталов.
* `Jekyll` остаётся неплохим выбором для практически любых проектов из-за долгой истории, множества плагинов и простоты использования, но постепенно теряет популярность.

### Сравнение характеристик

| Критерий | Docusaurus | MkDocs | Diplodoc | Sphinx | Hugo | Jekyll |
|----------|------------|---------|-----------|---------|------|--------|
| Скорость | Быстро | Очень быстро | Средне | Долго | Средне | Быстро |
| Сложность использования | Средняя | Низкая | Средняя | Высокая | Средняя | Низкая |
| Документация и сообщество | Отлично | Отлично | Средне | Отлично| Хорошо | Отлично |
| Экосистема | Много плагинов, MDX | Material theme, макросы | Плагины, совместимые с `markdown-it` | Есть все | Обширная стандартная библиотека, плагины | Плагины |
| Генерация OpenAPI | Встроенная поддержка, плагины | Плагины | Встроенная поддержка, без кастомизации | Больше всего вариантов | Плагины, стандартные средства | Плагины, стандартные средства |

## Подробный разбор

### Docusaurus

Разработчик и дата выпуска: Meta (Facebook), 2017 год | [Сайт](https://docusaurus.io/)

* Сложность использования: Средняя. Для базового использования достаточно знания Markdown, для кастомизации нужны знания React
* Документация и сообщество: Отличная документация, большое активное сообщество, множество примеров
* Локализация и версионирование: Встроенная поддержка
* Экосистема: Богатая. Поддержка MDX, множество плагинов, темы
* Переиспользование контента: MDX компоненты
* OpenAPI: Интеграция с Redocly, Redoc, поддержка Swagger UI, Docusaurus OpenAPI Plugin.
* Поиск: Встроенный локальный поиск + интеграция с Algolia DocSearch
* [Пример сайта: ClickHouse](https://clickhouse.com/docs)

**Мое мнение**:

Прекрасный инструмент, который сочетает в себе простоту и в то же время возможности для создания прекрасных сайтов. Есть возможность быстро начать использовать, добавив все необходимое для комфортного использования документации просто прописав несколько строк в конфигурационном файле — работающий поиск, простая локализация, версионирование, понятные плагины и многое другое.

Важнейшая часть для кастомизации — [MDX](https://mdxjs.com/). Это формат, который позволяет совмещать Markdown и JSX в одном файле и таким образом создавать любые сочетания текста и интерактивных элементов, в том числе используя переменные, условный рендеринг и возможности компонентного подхода.

Этот инструмент также хорошо подходит для создания целых сайтов, в которых документация — только один из разделов, и в таком случае получится сохранить единый стиль для всех частей продукта, причем этот стиль будет проработан фронтендерами с помощью привычных подходов.

### MkDocs

Разработчик и дата выпуска: Tom Christie, 2014 год | [Сайт](https://www.mkdocs.org/)

* Сложность использования: Низкая. Чистый Markdown с возможностью расширения через плагины, простая конфигурация в YAML
* Документация и сообщество: Хорошая документация, активное сообщество
* Локализация и версионирование: Через плагины
* Экосистема: Material theme значительно расширяет функциональность инструмента, множество плагинов
* Переиспользование контента: Макросы
* OpenAPI: Через плагины (swagger-ui)
* Поиск: Встроенный поиск в Material theme
* [Пример сайта: Видеонаблюдение Ростелеком](https://help.camera.rt.ru/)

**Мое мнение**:

Говорим MkDocs — чаще всего подразумеваем тему или фреймворк [Material for MkDocs](https://docs.readthedocs.io/en/stable/intro/mkdocs.html), я уже давно не видел проектов только на MkDocs без Material. В своей основе MkDocs это предельно простой генератор, я бы даже рискнул назвать его примитивным. А Material for MkDocs расширяет его функциональность, добавляя умный поиск, продвинутое форматирование, разные визуальные элементы вроде вкладок и аннотаций, поддержку диаграмм как кода и так далее.

Я использовал его для прототипирования сайта с документацией для одного из проектов по работе, и мне понадобилось меньше получаса чтобы показать уже собранный и готовый к выкладке сайт с несколькими страницами документации. Это быстро, понятно и довольно удобно, но в то же время не все готовы мириться с тем, как выглядит готовый сайт, и что кастомизировать его будет непросто.

### Diplodoc

Разработчик и дата выпуска: Яндекс, 2022 год | [Сайт](https://diplodoc.com/ru)

* Время развертывания: 30-45 минут
* Сложность использования: Средняя. Своя система шаблонов и форматирования
* Документация и сообщество: Базовая документация, небольшое русскоязычное сообщество
* Поддержка диаграмм: Встроенная поддержка (Mermaid)
* Локализация и версионирование: Нужно описывать конфигурацию самостоятельно, но поддержка в планах
* Экосистема: Любые плагины, совместимые с парсером [markdown-it](https://github.com/markdown-it/markdown-it). Самому с этим справиться непросто
* Переиспользование контента: Встроенный механизм на нескольких уровнях, от блоков до целых страниц
* OpenAPI: Встроенная поддержка, включая плейграунд
* Поиск: Интеграция с Lunr
* [Пример сайта: YDB Docs](https://ydb.tech/docs/ru/)

**Мое мнение**:

Это хороший инструмент, который сделан в первую очередь для средних и крупных проектов. В основе работы с Markdown - свой диалект (YFM), который даёт больше возможностей, чем практически у всех остальных инструментов в этом списке.

Помимо обычных статических страниц, можно декларативно описывать кастомные страницы (например разводящие страницы) с помощью [Page Constructor](https://diplodoc.com/docs/ru/project/page-constructor). Технический писатель может делать это самостоятельно, и эти страницы будут выглядеть действительно хорошо, как в [этом примере](https://diplodoc.com/docs/ru/project/pc-example1).

Для крупных проектов у этого инструмента есть некоторые особые возможности, например пресеты переменных, которые позволяют легко генерировать из одной текстовой базы несколько разных версий документации, а также хорошая производительность, которая позволяет собирать сайты из репозиториев объемом даже в пару гигабайт, знаю по своему опыту.

Diplodoc — это определенно не самый просто инструмент для самостоятельной настройки. Я знаю технических писателей, которые успешно с этим справляются и даже создают полноценные пайплайны для CI/CD, но не все могут это сделать.

### Sphinx

Разработчик и дата выпуска: Georg Brandl для Python Software Foundation, 2008 год | [Сайт](https://www.sphinx-doc.org/en/master/index.html#)

* Сложность использования: Высокая. Использует reStructuredText (хотя поддерживает и Markdown), сложная конфигурация
* Документация и сообщество: Обширная документация, большое устоявшееся сообщество
* Локализация и версионирование: Встроенная поддержка обеих функций, продвинутые инструменты для перевода
* Экосистема: Богатейшая экосистема расширений
* Переиспользование контента: Продвинутая система директив
* OpenAPI: Через расширения, множество способов
* Поиск: Встроенный поиск, возможность интеграции с внешними системами
* Дополнительные преимущества:
   * Превосходная поддержка LaTeX и PDF
   * Автоматическая генерация документации из кода (Docstrings)
   * Кросс-референсы между проектами
   * Семантическая разметка
* [Пример сайта: Linux Kernel](https://docs.kernel.org/)

**Мое мнение**:

Sphinx — это самый зрелый и гибкий инструмент в списке, с помощью которого можно решить практически любую задачу. С другой стороны, процесс решения точно не будет простым — у этого инструмента очень крутая кривая обучения. Однако, это окупается впоследствии, если он оказывается в руках человека или команды, обладающих достаточными техническими навыками.

Spinx появился как инструмент для документирования кода на Python, но давно вышел за пределы экосистемы и получил множество новых применений. В отличие от остальных инструментов, он позволяет работать как с Markdown, так и с reStructuredText, для которого был изначально создан. Markdown обрабатывается с помощью MyST-Parser, что позволяет еще и выбрать, какие элементы как нужно обрабатывать.

Также Sphinx из коробки позволяет автоматически генерировать документацию из комментариев в коде, причем с помощью разных стилей таких комментариев. А еще поддерживает LaTeX, экспорт в PDF, множество разных способов отображения справочников, API, возможность включать фрагменты кода из других проектов...

В общем, Sphinx подойдет для любых возможных задач для любых крупных и средних проектов, но для проектов меньших масштабов или при отсутствии людей, которые в состоянии справиться с его сложностью, он может принести немало головной боли.

### Hugo

Разработчик и дата выпуска: Steve Francia, 2013 год | [Сайт](https://gohugo.io/)

* Сложность использования: Средняя. Требует понимания Go templates для кастомизации
* Документация и сообщество: Подробная документация, активное сообщество
* Локализация и версионирование: Встроенная многоязычность, версионирование через ветки
* Экосистема: Множество тем и shortcodes
* Переиспользование контента: Partial templates, shortcodes
* OpenAPI: Через внешние инструменты и shortcodes
* Поиск: Через интеграции (Algolia, Lunr)
* Дополнительные преимущества:
   * Самая быстрая сборка среди SSG
   * Отличная производительность сайтов
* [Пример сайта: Ozon Docs](https://docs.ozon.ru/common)

**Мое мнение**:

Hugo лично у меня вызвал противоречивые чувства. Для работы он требует установки Go, а потом позволяет собирать сайты с помощью крошечного бинарника без внешних зависимостей — просто и элегантно. Скорость работы потрясающая, а с самого начала получается сделать красивый сайт стандартными средствами, в сам инструмент уже встроено практически все, что нужно для работы. Есть и свой парсер Markdown — Goldenmark, и shortcodes, с помощью которых можно легко переиспользовать контент и прочие атрибуты инструмента, который считается стандартом индустрии.

Но потом начинаются сложности, которые не дали мне как следует поисследовать Hugo в свободное время. После первых шагов хочется изучить возможности для кастомизации. Их у Hugo не просто много, а очень много. Вместо shortcodes можно использовать Partial templates, что требует понимания работы темплейтов в Go. Если темплейты Liquid (Jekyll, у Diplodoc аналогичный синтаксис) или Jinja2 мне оказались вполне понятны, то осмыслить темплейты в Go я так и не смог, хотя несколько раз пытался. Дальше появляются какие-то таксономии, функции, ресурсы страниц, хуки, модули и другие элементы.

Мне приходится поверить на слово, что это отличный инструмент. Мне понравился тестовый проект, но я сомневаюсь, что без разработчиков, владеющих Go, его можно без проблем использовать в продакшене.

### Jekyll

Разработчик и дата выпуска: Tom Preston-Werner (GitHub), 2008 год | [Сайт](https://jekyllrb.com/)

* Сложность использования: Низкая для базового использования, средняя для кастомизации
* Документация и сообщество: Хорошая документация, большое устоявшееся сообщество
* Локализация и версионирование: Базовая поддержка
* Экосистема: Множество плагинов и тем, особенно для блогов
* Переиспользование контента: Includes, layouts
* OpenAPI: Через плагины и интеграции
* Поиск: Через плагины (Lunr, Algolia)
* Дополнительные преимущества:
   * Нативная интеграция с GitHub Pages
   * Простота использования
   * Большое количество готовых тем
* [Пример сайта: Deckhouse](https://deckhouse.ru/products/kubernetes-platform/documentation/v1/)

**Мое мнение**:

Это был первый генератор статических сайтов, который я попробовал использовать, причем сделал это я еще до того как официально стал техническим писателем. В то время Ruby on Rails еще не вызывал удивления, и я с удовольствием поставил его себе в систему, ознакомился с концепцией Gems и сделал свой первый статический сайт (вроде бы блог). Не то чтобы это было просто, но результат мне вполне понравился.

Jekyll создавался в комьюнити Ruby, практически одновременно с GitHub, и они всегда были тесно связаны. Вы ведь наверняка неоднократно указывали `.nojekyll` при развертывании на GitHub Pages, правда? В те времена люди умели писать простую и понятную документацию, и руководства по Jekyll до сих пор остаются для меня примером.

За годы присутствия на рынке Jekyll популяризовал то, что потом использовалось в десятках других генераторов — Front Matter, шаблоны Liquid, includes и многое другое. Отличительной чертой Jekyll всегда была простота, которая до сих пор впечатляет, а наработки сообщества предлагают широкий выбор для кастомизации сайта.

Сейчас Jekyll редко является очевидным выбором для новых проектов. Он фактически прекратил развиваться, а сам Ruby из модного языка с крупным сообществом стал скорее экзотикой. Появились новые подходы и новые инструменты, предлагающие другие возможности, но классика всегда останется классикой.