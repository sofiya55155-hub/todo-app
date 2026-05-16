# Todo App Docker

Простое Flask-приложение для хранения задач.

Вариант дз2 - 3 вариант. Данный проект был выбран из-за его простоты и удобства работы с ним.

## Сборка

```bash
docker build -t my-app .
```

## Первый запуск

```bash
docker run -d -p 8080:8080 -v app-data:/data --name app my-app
```

## Открыть

http://localhost:8080

## Проверка сохранения данных

Остановить контейнер:

```bash
docker stop app
docker rm app
```

Запустить снова:

```bash
docker run -d -p 8080:8080 -v app-data:/data --name app my-app
```

## Логи

```bash
docker logs app
```


# Todo App

This is a simple Todo application built using Python and SQLite. The application allows users to add, view, and delete tasks. The data is stored in a SQLite database and the front-end is rendered using the Jinja2 template engine.

## Requirements
- Python 3.x
- Flask
- SQLite3

## Installation
1. Clone the repository git clone 

    `https://github.com/pj8912/todo-app.git`

2. Install the required packages
    
    `pip install -r requirements.txt`

3. Create the database
    
    `python db_create.py`

## Usage
1. Start the development server
    python app.py

2. Open `http://localhost:5000` in your web browser

