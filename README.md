# Kittygram

[![Kittygram CI/CD](https://github.com/MaksZakharov/kittygram_final/actions/workflows/main.yml/badge.svg)](https://github.com/MaksZakharov/kittygram_final/actions/workflows/main.yml)

## Описание проекта
**Kittygram** — это социальный сервис для любителей кошек. 

Пользователи могут:
- Создавать профили своих питомцев с фотографиями.
- Указывать достижения котиков (например, «Поймал мышь», «Самый пушистый»).
- Просматривать профили других пользователей и их питомцев.

Проект реализован в рамках обучения на Яндекс.Практикуме и демонстрирует навыки работы с Django, Docker и CI/CD.

## Стек технологий
- Python 3.10
- Django 3.2
- Django REST Framework
- PostgreSQL 13
- Gunicorn
- Nginx
- Docker & Docker Compose
- GitHub Actions (CI/CD)

## Установка и запуск
### 1. Клонирование репозитория
```bash
git clone git@github.com:MaksZakharov/kittygram_final.git
cd kittygram_final
```

### 2. Настройка переменных окружения
Создайте файл `.env` в корне проекта. Пример содержимого:

```env
# Настройки PostgreSQL
POSTGRES_DB=kittygram
POSTGRES_USER=kittygram_user
POSTGRES_PASSWORD=kittygram_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Django
SECRET_KEY=секретный_ключ_django
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost,example.com
```

> ⚠️ Значения `SECRET_KEY` и `POSTGRES_PASSWORD` должны быть уникальными и безопасными.

### 3. Запуск контейнеров
Для локального запуска используйте:
```bash
docker compose up -d
```

Для боевого запуска на сервере:
```bash
docker compose -f docker-compose.production.yml up -d
```

### 4. Миграции и статика
После запуска контейнеров выполните:
```bash
docker compose exec backend python manage.py migrate --noinput
docker compose exec backend python manage.py collectstatic --noinput
```

## CI/CD
- При push в любую ветку запускаются тесты (flake8, pytest).
- При push в `main` автоматически выполняется:
  - сборка Docker-образов для backend, frontend и gateway;
  - публикация образов на Docker Hub;
  - деплой проекта на удалённый сервер;
  - выполнение миграций и сборка статики;
  - уведомление в Telegram о завершении деплоя.

## Автор
- **Максим Захаров** — [MaksZakharov](https://github.com/MaksZakharov)

