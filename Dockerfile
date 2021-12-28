
FROM python:3.7.9

RUN apt-get update

RUN useradd taxijjang
RUN id

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER taxijjang
RUN id

RUN mkdir /code
COPY . /code
WORKDIR /code

RUN mkdir /static

RUN pip install --upgrade pip
RUN pip install --user -r requirements/requirements-dev.txt

RUN python manage.py collectstatic --noinput

#RUN mkdir -p run

#CMD gunicorn config.wsgi:application --bind unix:/code/run/gunicorn.sock --workers 4 --timeout=60 --log-file=-
