FROM python:3.7.9


RUN apt-get update

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements/requirements.txt /usr/src/app
COPY ./requirements/requirements-service.txt /usr/src/app
RUN pip install -r requirements-service.txt

COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=config.settings.test"]
