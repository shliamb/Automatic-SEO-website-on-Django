# Используем базовый образ Python версии 3.12-slim
FROM python:3.12-slim

# Копируем все файлы из текущего контекста сборки в текущую директорию в образе
COPY . .

# Обновляем pip и устанавливаем зависимости из requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Устанавливаем рабочую директорию
WORKDIR /app

# Используем CMD для указания команды, которая будет выполнена при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
