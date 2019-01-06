
FROM python:3.4.9-alpine3.8

ENV PROJECT_ROOT /opt/app

RUN mkdir -p /opt/app
WORKDIR /opt/app

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev

# COPY Pipfile Pipfile.lock /opt/app/

RUN pip install pipenv && pipenv install --dev --system

COPY . /opt/app/

COPY start.sh /start.sh

EXPOSE 8000

CMD ["/start.sh", "-docker"]
