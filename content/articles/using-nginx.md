+++
title = "Запускаем локальный сервер с nginx"
date = "2025-07-27"
draft = true

[taxonomies]
tags=["tools"]
+++

## Запускаем локальный сервер с nginx

анные есть. Клиент готов. Но где сервер?
Без сервера не будет ни запросов, ни ответов. Он — третья, и не менее важная, сторона веба. 

В этой части мы развернём собственный локальный веб-сервер с помощью nginx — простого, но мощного инструмента, который используется в реальных production-средах. Вы узнаете:

Что такое веб-сервер и зачем он нужен
Как он отдаёт файлы по HTTP
Что такое localhost, порты и статический контент
Как проверить работу сервера через браузер и curl
Мы поместим туда те же файлы, с которыми работали ранее, и увидим, как данные, полученные из API, становятся частью локального сайта. Это не имитация. Это реальный веб-сервер, который работает так же, как и те, что используются в облаке.

Понимание сервера позволяет:

Писать точные инструкции по развёртыванию
Понимать, как работает путь от файла к URL
Проверять, что документация соответствует реальной инфраструктурещ”

### 🖥️ Windows (рекомендуемая среда)

- Используйте **Git Bash** (входит в [Git for Windows](https://git-scm.com/download/win))
- Пути: `/c/nginx/html` (аналог `C:\nginx\html`)
- Запуск nginx: `start nginx`

### 🍏 macOS

- `curl` и терминал — встроены
- Установите nginx через Homebrew:  

  ```bash
  brew install nginx
  ```

Пути: /usr/local/etc/nginx/html
Запуск:

```bash
brew services start nginx
```

Проверка: <http://localhost>

🐧 Linux (Ubuntu/Debian)
Установите nginx:

```bash
sudo apt update && sudo apt install nginx
```

Пути: `/var/www/html`

Запуск:

```bash
sudo systemctl start nginx
```

Проверка: http://localhost

✅ На всех системах:

🎯 Цель
Разместить страницу на локальном сервере и увидеть, как она работает в "реальном" веб-окружении.

🛠️ Шаги
Windows
Скачайте nginx
Перейдите на https://nginx.org/download/
Скачайте nginx-1.24.0.zip
Распакуйте в C:\nginx
Копируем файлы через проводник
Откройте C:\web-tutorial
Скопируйте:
index.html
post.json
Вставьте в: C:\nginx\html
Запускаем сервер через Git Bash

cd /c/nginx
start nginx

Проверяем в браузере
→ http://localhost
Проверяем через curl

curl -I http://localhost

Ожидаемый ответ:



1
2
3
HTTP/1.1 200 OK
Server: nginx/1.24.0
...
Проверим файл:

curl http://localhost/post.json | head -n 5

macOS / Linux
Выполните те же шаги, но с учётом путей и команд:

macOS:
bash

brew install nginx
cp ~/web-tutorial/* /usr/local/share/nginx/html/
brew services start nginx

Linux:
bash


1
2
sudo cp ~/web-tutorial/* /var/www/html/
sudo systemctl start nginx

### Save queries

```bash
# Установи json-server (требует Node.js)
npm install -g json-server

# Создай db.json
echo '{"posts": []}' > db.json

# Запусти сервер
json-server --watch db.json
```
