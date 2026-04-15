# Kittygram — Social Network for Pet Photos

Веб-сервис для публикации фотографий питомцев с возможностью взаимодействия пользователей.

## Описание проекта

Проект реализует платформу для обмена фотографиями питомцев.

Позволяет:
- публиковать фотографии с описанием и тегами
- просматривать ленту пользователей
- взаимодействовать с контентом (лайки)
- управлять пользовательскими аккаунтами

## Что реализовал

- Разработал REST API на Django REST Framework
- Реализовал модели данных:
  - пользователи
  - питомцы (фото, описание, теги)
- Настроил сериализаторы и API endpoints
- Реализовал бизнес-логику:
  - публикация и редактирование контента
  - система лайков
- Подключил PostgreSQL через Docker
- Настроил работу со статикой и медиа (Nginx)
- Настроил production-окружение:
  - Gunicorn + Nginx
- Реализовал контейнеризацию (Docker, docker-compose)
- Настроил CI/CD:
  - запуск тестов и линтера
  - автоматический деплой на сервер (GitHub Actions)

## Основные возможности

- Регистрация и аутентификация пользователей
- Публикация фотографий питомцев
- Добавление описаний и тегов
- Просмотр ленты
- Система лайков
- Работа с медиа-контентом

## Технологический стек

Backend: Python 3.10, Django, Django REST Framework  
База данных: PostgreSQL  
Инфраструктура: Docker, docker-compose, Gunicorn, Nginx  
CI/CD: GitHub Actions  

## Деплой

Проект развёрнут на сервере с использованием Docker, Gunicorn и Nginx.  
Настроен CI/CD pipeline для автоматического тестирования и деплоя.

## Установка и запуск

```bash
git clone git@github.com:<ваш_логин>/kittygram_final.git
cd kittygram_final
```

### Переменные окружения

Создайте файл `.env`:

```
SECRET_KEY=<django_secret_key>
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost

POSTGRES_DB=kittygram
POSTGRES_USER=kittygram_user
POSTGRES_PASSWORD=kittygram_password
DB_HOST=db
DB_PORT=5432
```

### Запуск

```bash
docker compose up -d --build
```

### Подготовка приложения

```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic --noinput
docker compose exec backend python manage.py createsuperuser
```

## Примеры API

Создание пользователя  
POST /api/users/

Получение списка котиков  
GET /api/cats/

Добавление котика  
POST /api/cats/

## Планы по доработке

- Добавить систему комментариев
- Реализовать подписки между пользователями
- Добавить уведомления
- Оптимизировать работу с медиа (CDN)
- Расширить тестовое покрытие
