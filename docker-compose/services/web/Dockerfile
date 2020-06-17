FROM python:3.8.1-slim-buster

WORKDIR /usr/src/app

RUN apt update -y && apt install postgresql-client -y

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/
