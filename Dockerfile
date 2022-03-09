FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install pipenv
COPY ./Pipfile ./
COPY ./Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./src .

