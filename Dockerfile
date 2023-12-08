FROM python:3.12-slim

# Устанавливаем переменную окружения для отключения вывода журнала Python
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/

COPY . /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


