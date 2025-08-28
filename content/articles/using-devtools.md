+++
title = "Заполняем текстовое поле через DevTools"
date = "2025-07-27"
draft = true

[taxonomies]
tags=["tools"]
+++

## Заполняем текстовое поле через DevTools
🎯 Цель
Понять, как браузер загружает данные и как можно вручную управлять контентом с помощью инструментов разработчика.

Сервер отдаёт данные. Браузер их получает. А что происходит между ними?
Как "голый" JSON превращается в страницу, которую видит пользователь? И как технический писатель может "заглянуть под капот" и увидеть, что именно происходит? 

В этой части мы перейдём на сторону клиента — туда, где живут HTML, CSS и JavaScript. Мы не будем писать сложные приложения. Вместо этого мы:

Создадим простейшую страницу с текстовым полем
Увидим, как браузер запрашивает данные с сервера
Научимся вручную управлять контентом через инструменты разработчика (DevTools)
Поймём, как fetch() заменяет curl в браузере
Ключевой момент: вы не обязаны писать код, чтобы понимать, как он работает. С помощью DevTools вы можете:

Видеть каждый сетевой запрос
Проверять ответы API
Запускать JavaScript вручную
Моделировать ошибки и проверять поведение
Это особенно важно для технического писателя: вы сможете самостоятельно тестировать примеры, понимать, что видит пользователь, и делать скриншоты с реальными данными, а не "заглушками".

🛠️ Шаги
Создаём index.html
Создайте файл в папке ~/web-tutorial:
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>JSON Viewer</title>
</head>
<body>
  <h1>Данные из API</h1>
  <textarea id="json-output" rows="15" cols="80" placeholder="Здесь появятся данные..."></textarea>
</body>
</html>

Открываем в браузере
Дважды кликните на index.html → откроется в Chrome, Edge или Firefox.

Открываем DevTools
Нажмите F12 или ПКМ → "Просмотреть код".

Переходим на вкладку Console
В консоли введите:

fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => response.json())
  .then(data => {
    document.getElementById('json-output').value = JSON.stringify(data, null, 2);
  })
  .catch(error => {
    document.getElementById('json-output').value = 'Ошибка: ' + error.message;
  });

→ Поле заполнится отформатированным JSON.

Проверяем запрос в Network
Перейдите на вкладку Network
Обновите страницу
Нажмите команду в консоли
В списке появится posts/1 → статус 200
Кликните на него → во вкладке Response увидите JSON.

Экспериментируем
Замените posts/1 на posts/5, users/1
Попробуйте posts/9999 → увидите ошибку 404
В поле появится: Ошибка: Failed to fetch
💡 Это помогает понять, как пользователь видит ошибки в документации. 

```javascript
fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    title: 'Мой пост',
    body: 'Тестовый текст',
    userId: 1
  })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Ошибка:', error));
```
