# Dockerfile
#FROM python:3.10.4-alpine3.15
#Version ligera de python
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

#RUN apk update \
#   && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
#   && pip install --upgrade pip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

#0.0.0.0:8000 para que entren de otros lados
CMD python manage.py runserver 0.0.0.0:8000