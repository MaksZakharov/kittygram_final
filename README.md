# Kittygram

Kittygram — это социальная сеть для обмена фотографиями котиков, созданная в рамках обучения на курсе **Python-разработчик+** (Яндекс Практикум).  
Проект разворачивается в контейнерах Docker и поддерживает полный цикл CI/CD.

![Kittygram](/assets/img/kittygram.png)

---

## Описание

Платформа позволяет пользователям:
- Регистрироваться и авторизоваться
- Загружать фотографии своих питомцев
- Просматривать галерею котиков
- Ставить лайки
- Добавлять описания и теги

Проект развернут на сервере с использованием Docker, GitHub Actions и Nginx.

---

## Технологии

- Python 3.10  
- Django 3.2  
- Django REST Framework  
- PostgreSQL  
- Docker & Docker Compose  
- Nginx + Gunicorn  
- GitHub Actions (CI/CD)  

---

## Что сделал

- Реализовал модели пользователей и котиков  
- Настроил сериализаторы и API для работы с котиками  
- Подключил базу данных PostgreSQL через Docker  
- Настроил статику и медиа-файлы через Nginx  
- Настроил Gunicorn для продакшн-развёртывания  
- Настроил CI/CD с GitHub Actions: тесты, линтер, автодеплой на сервер  
- Оформили контейнеризацию всего проекта (`docker-compose`)  

---

## Как запустить проект локально

### 1. Клонировать репозиторий
```bash
git clone git@github.com:<ваш_логин>/kittygram_final.git
cd kittygram_final
```

### 2. Создать файл `.env`
```dotenv
SECRET_KEY=<django_secret_key>
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost
POSTGRES_DB=kittygram
POSTGRES_USER=kittygram_user
POSTGRES_PASSWORD=kittygram_password
DB_HOST=db
DB_PORT=5432
```

### 3. Собрать и запустить контейнеры
```bash
docker compose up -d --build
```

### 4. Выполнить миграции и собрать статику
```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic --noinput
```

### 5. Создать суперпользователя
```bash
docker compose exec backend python manage.py createsuperuser
```

---

## CI/CD

- При пуше в ветку `main` автоматически запускаются тесты и линтер  
- После успешной проверки проект деплоится на сервер  
- Используются **GitHub Actions**, **Docker Hub**, **Nginx** и **Gunicorn**  

---

## Автор

**Макс Захаров**  
Python backend developer (в процессе обучения)
