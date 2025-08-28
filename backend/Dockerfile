# Базовый образ Python
FROM python:3.9-slim

# Устанавливаем зависимости для работы с PostgreSQL и Pillow
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev musl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir

# Копируем весь проект внутрь контейнера
COPY . .

# Собираем статику (на всякий случай, чтобы образ был самодостаточный)
RUN python manage.py collectstatic --noinput || true

# Запускаем через gunicorn
CMD ["gunicorn", "kittygram_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
