FROM python:3.7.9

RUN apt-get update

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
COPY . /code
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install -r requirements/requirements-dev.txt

RUN python manage.py collectstatic --no-input --clear

#RUN mkdir -p run

#CMD gunicorn config.wsgi:application --bind unix:/code/run/gunicorn.sock --workers 4 --timeout=60 --log-file=-