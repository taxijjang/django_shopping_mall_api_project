FROM python:3.7.9

RUN apt-get update

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

COPY . /code
WORKDIR /code

RUN mkdir /static
RUN mkdir /staticfiles

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements/requirements-dev.txt

#RUN python manage.py collectstatic --noinput