+++
title = "Локализация чисел, валют и дат"
date = 2025-07-29

aliases = [
    "/localize-currencies-dates/",
]

[taxonomies]
tags=["guidelines"]

[extra]
comment = true
+++

# Локализация чисел, валют и дат

Форматирование влияет на восприятие и доверие к информации, особенно представленной в документации. Это простая вещь, но в ней есть нюансы.

Для веб-платформ существуют единые стандарты отображения данных:

* [Intl API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl) в браузерах и JavaScript (часть стандарта [ECMAScript](https://262.ecma-international.org/)).

* [Unicode CLDR](https://cldr.unicode.org/) (Common Locale Data Repository) - универсальный стандарт, лежащий в основе `Intl API`. `Intl.NumberFormat`, `Intl.DateTimeFormat` и другие компоненты этого API используют локализационные данные из Unicode CLDR.

`Intl` поддерживается всеми современными браузерами и по умолчанию применяется для локализации контента. За счет использования данных из Unicode CLDR этот механизм также обеспечивает соответствие национальным стандартам — ISO, ГОСТ и прочим.

## Интерактивный пример

Для простоты при выборе локали предполагается, что в локали `Ru` валюта — это рубли, а в `En` — доллары. О нюансах форматирования валют в разных локалях рассказано далее.

<div class="currency-container">
    <div class="selectors">
        <select id="typeSelector">
            <option value="number">Число</option>
            <option value="currency" selected>Валюта</option>
            <option value="date">Дата</option>
        </select>
        <select id="localeSelector">
            <option value="ru" selected>Ru</option>
            <option value="en">En</option>
        </select>
    </div>
    <div class="fields">
        <input type="text" id="inputField" placeholder="Введите значение">
        <input type="text" id="outputField" placeholder="Результат"readonly>
    </div>
    <button type="button" class="format-btn" onclick="formatValue()">Форматировать</button>
    <div id="errorMessage" class="error"></div>
</div>

## Как форматировать числа, валюты и даты

Будут рассмотрены локали `ru-RU` и `en-US`. Подробнее о числах и валютах см. [CLDR: Number and currency patterns](https://cldr.unicode.org/translation/number-currency-formats/number-and-currency-patterns), о датах — [CLDR: Date/Time Patterns](https://cldr.unicode.org/translation/date-time/date-time-patterns).

### Числа и валюты

* В `ru-RU` используется **запятая** как разделитель дробной части и **пробел** для тысяч.
* В `en-US` — **точка** для дробной части и **запятая** для тысяч.
* Символ для обозначения валюты ставится **перед** числом без пробела в англоязычной среде, а в русскоязычной — **после** и с пробелом.

| Категория | `ru-RU` | `en-US` |
|--------|--------|--------|
| **Число** | `1 234,567` | `1,234.567` |
| **Рубли** | `1 234,56 ₽` | `₽1,234.56` |
| **Доллары** | `1 234,56 $` | `$1,234.56` |

### Дата

| Категория | `ru-RU` | `en-US` |
|--------|--------|--------|
| **Дата** | `06.07.2024` | `7/6/2024` |
| **Дата и время** | `06.07.2024, 14:30:00` | `7/6/2024, 2:30:00 PM` |
| **Дата**<br/>(строковый формат) | `6 июля 2024 г.` | `July 6, 2024` |

В `en-US`:

* Нули в начале числового кода дня и месяца пропускаются.
* Обязателен пробел между числом и `AM/PM`. `2:30 PM` — правильно, `2:30PM` — неправильно.
* Для большей точности в локализованных строках можно добавлять обозначения PDT (Pacific Daylight Time) и PST (Pacific Standard Time), являющиеся аналогами летнего и зимнего времени. PDT это часовой пояс UTC−7, PST — UTC-8. Мне никогда не приходилось применять их, но об их существовании полезно знать.

## Работа с датами: универсальный формат для хранения и передачи

Для работы с API и в других случаях, когда нужно обеспечить машиночитаемость, не должны использоваться локализованные строки из примеров выше. Вместо них рекомендуется использовать даты, соответствующие [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) в UTC:

```text
2024-07-06T14:30:00Z
```

Расшифровка:

| Часть | Значение | Пояснение |
|------|---------|----------|
| `2024` | Год | Четырёхзначный год |
| `07` | Месяц | Июль (всегда двузначный: 01–12) |
| `06` | День | 6-е число месяца (01–31) |
| `-` | Разделитель | Статический разделитель года, месяца и дня |
| `T` | Маркер времени | Обозначает начало временной части (от *Time*) |
| `14` | Часы | 14 часов в 24-часовом формате (2:30 PM) |
| `30` | Минуты | 30 минут |
| `00` | Секунды | 00 секунд |
| `Z` | Временная зона | Обозначает **UTC** (*Zero offset*, нулевое смещение) |

Последняя буква `Z`, обозначающая временную зону, применяется для указания времени по Гринвичу, то есть в часовом поясе UTC+0. В других временных зонах нужно явно указывать смещение в часах и минутах в форматах `+HH:MM` или `-HH:MM`.

Примеры:

* `2024-07-06T14:30:00Z` — UTC+0 (Гринвич);
* `2024-07-06T17:30:00+03:00` — то же самое время, но в часовом поясе Москвы (UTC+3);
* `2024-07-06T07:30:00-07:00` — то же самое время, но в часовом поясе Нью-Йорка, Лос-Анжелеса или Торонто (UTC-7).

<script>
    function validateInput(value, type) {
        const errorElement = document.getElementById('errorMessage');
        const inputElement = document.getElementById('inputField');
        errorElement.textContent = '';
        inputElement.classList.remove('input-error');
        if (!value.trim()) {
            return false;
        }
        if (type === 'number' || type === 'currency') {
            if (value.includes('-')) {
                errorElement.textContent = 'Отрицательные числа не допускаются';
                inputElement.classList.add('input-error');
                return false;
            }
            const numberPattern = /^[\d\s.,]+$/;
            if (!numberPattern.test(value)) {
                errorElement.textContent = 'Некорректный формат числа';
                inputElement.classList.add('input-error');
                return false;
            }
            return true;
        }
        if (type === 'date') {
            // Проверяем оба формата дат
            const ruDatePattern = /^\d{1,2}\.\d{1,2}\.\d{4}$/;
            const enDatePattern = /^\d{1,2}\/\d{1,2}\/\d{4}$/;
            if (!ruDatePattern.test(value) && !enDatePattern.test(value)) {
                errorElement.textContent = 'Неверный формат даты. Используйте dd.mm.yyyy или mm/dd/yyyy';
                inputElement.classList.add('input-error');
                return false;
            }
            return true;
        }
        return false;
    }
    function parseNumber(value) {
        return parseFloat(value.replace(/\s/g,'').replace(',', '.'));
    }
    function formatNumber(number, locale) {
        if (locale === 'ru') {
            return number.toLocaleString('ru-RU');
        } else {
            return number.toLocaleString('en-US');
        }
    }
    function formatCurrency(number, locale) {
        if (locale === 'ru') {
            return number.toLocaleString('ru-RU', {
                style: 'currency',
                currency: 'RUB'
            });
        } else {
            return number.toLocaleString('en-US', {
                style: 'currency',
                currency: 'USD'
            });
        }
    }
    function parseDate(dateString) {
        // Определяем формат и парсим дату
        if (dateString.includes('.')) {
            // Формат dd.mm.yyyy (русский)
            const parts = dateString.split('.');
            return new Date(parts[2], parts[1] - 1, parts[0]);
        } else if (dateString.includes('/')) {
            // Формат mm/dd/yyyy (английский)
            const parts = dateString.split('/');
            return new Date(parts[2], parts[0] - 1, parts[1]);
        }
        return null;
    }
    function formatDate(dateString, outputLocale) {
        const date = parseDate(dateString);
        if (!date || isNaN(date.getTime())) {
            throw new Error('Некорректная дата');
        }
        if (outputLocale === 'ru') {
            return date.toLocaleDateString('ru-RU');
        } else {
            return date.toLocaleDateString('en-US');
        }
    }
    function formatValue() {
        const inputValue = document.getElementById('inputField').value;
        const type = document.getElementById('typeSelector').value;
        const locale = document.getElementById('localeSelector').value;
        const outputField = document.getElementById('outputField');
        if (!validateInput(inputValue, type)) {
            outputField.value = '';
            return;
        }
        try {
            let formattedValue = '';
            if (type === 'number') {
                const number = parseNumber(inputValue);
                if (isNaN(number)) {
                    throw new Error('Некорректное число');
                }
                formattedValue = formatNumber(number, locale);
            } else if (type === 'currency') {
                const number = parseNumber(inputValue);
                if (isNaN(number)) {
                    throw new Error('Некорректное число');
                }
                formattedValue = formatCurrency(number, locale);
            } else if (type === 'date') {
                formattedValue = formatDate(inputValue, locale);
            }  
            outputField.value = formattedValue;
        } catch (error) {
            document.getElementById('errorMessage').textContent = error.message || 'Ошибка форматирования';
            document.getElementById('inputField').classList.add('input-error');
            outputField.value = '';
        }
    }
    document.getElementById('typeSelector').addEventListener('change', function() {
        document.getElementById('errorMessage').textContent = '';
        document.getElementById('inputField').classList.remove('input-error');
        document.getElementById('outputField').value = '';
    });
    document.getElementById('localeSelector').addEventListener('change', function() {
        document.getElementById('errorMessage').textContent = '';
        document.getElementById('inputField').classList.remove('input-error');
        document.getElementById('outputField').value = '';
    });
</script>
