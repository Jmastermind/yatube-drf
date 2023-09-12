# YaTube RESTful API

API проекта "Yatube для блоггеров" на основе DRF.

## Технологии

- Python 3.9.10
- Django 4.2.5
- DRF 3.14.0
- SQLite
- JWT

## Используемые стандарты

- REST
- pep8
- flake8
- black
- pymarkdown
- mypy

## Установка

1. Склонируйте проект в рабочую директорию.
2. Создайте виртуальное окружение.
3. Установите зависимости из файла `requirements.txt`.
4. Выполните миграции и запустите сервер в режиме разработчика
   (находясь в директории `yatube_api`):

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

## Аутентификация

Для использования API необходимо зарегистрировать пользователя в БД приложения
через веб-интерфейс или командную строку. Затем получить JWT-токен.

 ```http
 POST http://127.0.0.1:8000/api/v1/jwt/create/
 content-type: application/json

 {
     "username": "username",
     "password": "password"
 }
 ```

## Документация для API

http://127.0.0.1:8000/redoc/
