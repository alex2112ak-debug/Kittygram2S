### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram2.git
```

```
cd kittygram2
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

# API «Потерян/Найден»

REST API для размещения объявлений о пропажах и находках с фотографиями.

## Технологии
- Python 3.10, Django 3.2, DRF
- JWT-аутентификация (djoser + simplejwt)
- Docker, Docker Compose
- SQLite (разработка)

## Запуск через Docker
Скопируйте `.env.example` в `.env` и при необходимости измените.
Выполните:
   ```bash
   docker-compose up --build
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser

API доступно по адресу http://localhost:8000/

Документация Swagger: http://localhost:8000/api/docs/

Основные эндпоинты
GET /announcements/ – список объявлений (фильтры: ?type=lost, ?status=open)

POST /announcements/ – создать объявление (только авторизованные)

GET /announcements/{id}/ – детали объявления

PUT/PATCH /announcements/{id}/ – редактировать (только владелец)

DELETE /announcements/{id}/ – удалить (только владелец)

POST /announcements/{id}/close/ – закрыть объявление (владелец)

POST /announcements/{id}/add_photo/ – добавить фото (владелец)

GET /announcements/{id}/photos/ – список фото

Тестовые запросы
Используйте файл requests.http (REST Client для VS Code) или импортируйте коллекцию Postman.

Валидации
Заголовок ≥ 3 символа

Описание ≥ 10 символов

Фото: форматы JPEG/PNG, размер ≤ 5 МБ

text

---

### 15. Последовательность действий для интеграции

1. **Скопируйте все указанные файлы** в соответствующие директории.
2. **Установите зависимости** (если запускаете без Docker):
   ```bash
   pip install -r requirements.txt
Выполните миграции:

bash
python manage.py makemigrations announcements
python manage.py migrate
Создайте суперпользователя (опционально):

bash
python manage.py createsuperuser
Запустите сервер:

Через Docker: docker-compose up --build

Локально: python manage.py runserver

Протестируйте API с помощью requests.http или Postman.