# Используем базовый образ Python
FROM python:3.8-slim

# Устанавливаем переменную окружения для работы внутри контейнера
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы в контейнер (requirements.txt и весь остальной код)
COPY requirements.txt /app/
COPY . /app/

# Устанавливаем зависимости
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Очищаем временные данные
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Команда для запуска приложения при старте контейнера
CMD ["/app/venv/bin/python", "app.py"]
