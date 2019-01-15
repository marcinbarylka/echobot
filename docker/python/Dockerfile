FROM python:3.6
WORKDIR /usr/src/app
RUN groupadd --gid 1002 unicorn \
  && useradd --uid 1002 --gid unicorn --shell /bin/bash --create-home unicorn
COPY Pipfile ./
COPY Pipfile.lock ./
RUN apt-get update --fix-missing
RUN apt-get upgrade -y
ENV PYTHONBUFFERED 1
RUN pip install pipenv
RUN pipenv install --system --deploy
RUN pipenv install gunicorn flake8
USER unicorn
