FROM python:3.10-slim

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=cfehome.settings.development

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY /backend ./backend

# Copy the GCP credentials file into the container
COPY app-compat-test.json ./backend/

WORKDIR /app/backend

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "/cfehome/wsgi:application"]


# # Base stage for common setup
# FROM python:3.10-slim as base
# EXPOSE 8000
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --upgrade pip && pip install -r requirements.txt
# COPY ./backend /app/backend
# WORKDIR /app/backend

# # Development stage
# FROM base as development
# ENV DJANGO_SETTINGS_MODULE=cfehome.settings.development
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# # Production stage
# FROM base as production
# ENV DJANGO_SETTINGS_MODULE=cfehome.settings.production
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "cfehome.wsgi:application"]
