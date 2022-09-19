### О проекте:

Данный проект является классическим примером отзовика с возможностями API.
В качестве фреймворка использовался Django 2.2.16.
Дополнительно использовались следующие пакеты: Django-filter 22.1, Django REST framework 3.12.4, Simple JWT 4.7.2.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Nedrya/api_yamdb
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

Заполнить базу данных тестовыми данными:

```
python3 manage.py install_bd
```


Запустить проект:

```
python3 manage.py runserver
```


### Информация:

Регистрация:
Регистрация происходит путем отправки POST запроса с указание пользовательского имени и адреса электронной почты.

Пример запроса регистрации нового пользрвателя:
```
POST http://127.0.0.1:8000/api/v1/auth/signup/
Content-Type: application/json

{
    "username": "1112",
    "email": "1112@qwe.ru"
}
```

Пример ответа:
```
{
  "email": "1112@qwe.ru",
  "username": "1112"
}
```

После успешной регистрации на почту придет секретный код, который позволит подтвердить почту и получить токен аутентификации.
Пример секретного кода: MSBrKI8ZkD


Подтверждение адреса электронной почты и получение токена аутентификации:

Пример запроса:
```
POST http://127.0.0.1:8000/api/v1/auth/signup/
Content-Type: application/json

{
    "username": "1112",
    "confirmation_code": "MSBrKI8ZkD"
}
```

Пример ответа:
```
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3NjEyMzg1LCJqdGkiOiJiNjI4N2Y3Y2JhMGQ0ZThjOGM3NGM2MTcwMDI4NjdkMCIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoiMTExMiIsImNvbmZpcm1hdGlvbl9jb2RlIjoiTVNCcktJOFprRCJ9.5wo80prs8WWwIZrsESG-fL9xl0jfNSYVq5mdFdpIVxs"
}
```

Подробнее с примерами запросов можно ознакомиться по ссылке http://127.0.0.1:8000/redoc/ .

Автор проекта: Недря Сергей
