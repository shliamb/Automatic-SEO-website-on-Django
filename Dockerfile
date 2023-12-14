FROM python:3.12-slim

# Устанавливаем переменную окружения для отключения вывода журнала Python
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 

WORKDIR /apps

COPY ./requirements.txt /apps/

COPY ./src /apps/

RUN pip install --upgrade pip && pip install -r requirements.txt

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
