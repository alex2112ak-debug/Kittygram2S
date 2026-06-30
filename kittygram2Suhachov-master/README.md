# Kittygram

Платформа для публикации фотографий домашних питомцев и обмена информацией между пользователями. Проект позволяет создавать профили питомцев, публиковать фотографии и взаимодействовать с дополнительными сервисами, расширяющими функциональность приложения.

В рамках творческого задания в проект добавлен модуль «Потерян/Найден», предназначенный для размещения объявлений о пропавших и найденных домашних животных.


# Возможности проекта
## Базовый функционал Kittygram
 - регистрация и авторизация пользователей;
 - создание и управление профилями питомцев;
 - публикация фотографий питомцев;
 - просмотр контента других пользователей.
## Дополнительный модуль «Потерян/Найден»
 - создание объявлений о пропаже или находке питомца;
 - добавление описания, места и контактной информации;
 - прикрепление фотографий;
 - поиск и фильтрация объявлений;
 - закрытие объявления после решения проблемы.

## Технологии
 - Python 3.13
 - Django 4.2
 - Django REST Framework
 - Djoser
 - Simple JWT
 - SQLite
 - Docker, Docker Compose

### Как запустить проект:

#### Клонировать репозиторий и перейти в папку проекта:

```
git clone https://github.com/alex2112ak-debug/Kittygram2S.git
```

```
cd Kittygram2S/kittygram2Suhachov-master
```

#### Cоздать и активировать виртуальное окружение:

```
py -3.13 -m venv env
```

```
env\Scripts\activate
```

#### Установить зависимости из файла requirements.txt:


```
pip install --upgrade pip
pip install -r requirements.txt
```

#### Создать .env файл

```
copy .env.example .env
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```



## Запуск через Docker

```bash
   docker-compose up --build
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
```

### API доступно по адресу 
```
http://localhost:8000/
```

### Документация Swagger: 
```
http://localhost:8000/api/docs/
```


## Основные эндпоинты Kittygram

### Авторизация
- `POST /auth/users/` — регистрация пользователя;
- `POST /auth/jwt/create/` — получение JWT-токена;
- `POST /auth/jwt/refresh/` — обновление токена;
- `POST /auth/jwt/verify/` — проверка токена.

### Пользователи
- `GET /users/` — список пользователей;
- `GET /users/{id}/` — информация о пользователе.

### Котики
- `GET /cats/` — список котиков;
- `POST /cats/` — создать профиль котика;
- `GET /cats/{id}/` — получить информацию о котике;
- `PUT/PATCH /cats/{id}/` — изменить информацию о котике;
- `DELETE /cats/{id}/` — удалить котика.

### Достижения
- `GET /achievements/` — список достижений;
- `POST /achievements/` — создать достижение;
- `PUT/PATCH /achievements/{id}/` — изменить достижение;
- `DELETE /achievements/{id}/` — удалить достижение.

## Дополнительный модуль «Потерян/Найден»

- `GET /announcements/` — список объявлений;
- `POST /announcements/` — создать объявление;
- `GET /announcements/{id}/` — детали объявления;
- `PUT/PATCH /announcements/{id}/` — редактировать объявление;
- `DELETE /announcements/{id}/` — удалить объявление;
- `POST /announcements/{id}/close/` — закрыть объявление;
- `POST /announcements/{id}/add_photo/` — добавить фотографию;
- `GET /announcements/{id}/photos/` — получить список фотографий объявления.

## Дополнительные возможности API

### Фильтрация котиков
- `GET /cats/?color=Black`
- `GET /cats/?birth_year=2022`

### Поиск котиков
- `GET /cats/?search=Барсик`

### Сортировка
- `GET /cats/?ordering=name`
- `GET /cats/?ordering=-birth_year`

### Фильтрация объявлений
- `GET /announcements/?type=lost`
- `GET /announcements/?status=open`
- `GET /announcements/?search=рыжий`

## Валидации

### Kittygram
- имя кота должно быть уникальным для одного владельца;
- год рождения должен быть корректным;
- имя кота не может совпадать с его цветом.

### Модуль «Потерян/Найден»
- заголовок объявления содержит минимум 3 символа;
- описание содержит минимум 10 символов;
- допускаются только изображения форматов JPG, JPEG и PNG;
- размер изображения не должен превышать 5 МБ.

## Тестирование

Для проверки API можно использовать:
- Swagger: `http://localhost:8000/api/docs/`
- ReDoc: `http://localhost:8000/api/redoc/`
- Postman;
- файл `requests.http` для VS Code.

## Переменные окружения (.env.example)

Проект использует переменные окружения для хранения конфиденциальных и конфигурационных данных.

Пример `.env.example`:

```
SECRET_KEY=django-insecure-change-me-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

ACCESS_TOKEN_LIFETIME_MINUTES=1440
REFRESH_TOKEN_LIFETIME_DAYS=7
```

### Описание переменных

- `SECRET_KEY` — секретный ключ Django
- `DEBUG` — режим отладки (True/False)
- `ALLOWED_HOSTS` — разрешённые хосты
- `DB_ENGINE` — движок базы данных
- `DB_NAME` — имя базы данных
- `DB_USER` — пользователь БД (если используется)
- `DB_PASSWORD` — пароль БД
- `DB_HOST` — хост базы данных
- `DB_PORT` — порт базы данных
- `ACCESS_TOKEN_LIFETIME_MINUTES` — время жизни access JWT токена
- `REFRESH_TOKEN_LIFETIME_DAYS` — время жизни refresh токена