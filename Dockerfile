
FROM python:3.4

ENV PROJECT_ROOT /usr/src/app

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock /usr/src/app/
RUN pip install pipenv && pipenv install --dev --system

COPY . /usr/src/app/

COPY start.sh /start.sh

EXPOSE 8000

CMD ["/start.sh", "-docker"]
