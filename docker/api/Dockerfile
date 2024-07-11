FROM --platform=linux/amd64 tiangolo/uwsgi-nginx-flask:python3.10

SHELL ["/bin/bash", "-c"]

COPY ../app /app
COPY ./docker/api/requirements.txt /app/
COPY ./docker/api/uwsgi.ini /app/

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y \
    python3-mysqldb python3-pymysql && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install -r requirements.txt
