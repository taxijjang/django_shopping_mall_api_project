
FROM python:3.7.9

RUN apt-get update

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
COPY . /code
WORKDIR /code

RUN mkdir /static

RUN pip install --upgrade pip
RUN pip install --user -r requirements/requirements-dev.txt

RUN python manage.py collectstatic --noinput