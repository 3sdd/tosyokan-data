FROM python:3.11-slim-bullseye

RUN apt-get update && \
    pip install --upgrade pip


COPY src /app
WORKDIR /app

RUN pip install -r /app/src/requirements.txt

