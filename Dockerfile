FROM python:3.7.9

RUN apt-get update

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
RUN mkdir /code/static
RUN mkdir /code/staticfiles
COPY . /code
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements/requirements-dev.txt

RUN python manage.py collectstatic --noinput
