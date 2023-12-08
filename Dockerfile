FROM python:3.12-slim

#WORKDIR /app

COPY . .

RUN pip install --upgrade pip -- only first time

#RUN pip install -r requirements.txt
RUN pip install -r requirements.txt && python manage.py runserver 0.0.0.0:8000

#command: bash -c "pip install -r requirements.txt && python manage.py runserver 0.0.0.0:8000"

#CMD ["python", "app.py"]