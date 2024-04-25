FROM python:3.10-slim

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY /backend ./backend

# Copy the GCP credentials file into the container
COPY app-compat-test.json ./backend/

WORKDIR /app/backend

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
