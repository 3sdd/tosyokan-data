# 参考: https://github.com/duck-nukem/django-in-docker-starter/blob/master/Dockerfile
FROM python:3.11-slim-bullseye

RUN apt-get update && \
    pip install --upgrade pip


COPY src/requirements.txt /app/src/requirements.txt

WORKDIR /app/src

RUN pip install -r /app/src/requirements.txt
