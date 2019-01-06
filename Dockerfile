
FROM python:3.4.9-alpine3.8

ENV PROJECT_ROOT /opt/app

RUN mkdir -p /opt/app
WORKDIR /opt/app

# RUN apk add --no-cache --virtual .build-deps \
#     ca-certificates gcc postgresql-dev linux-headers musl-dev \
#     libffi-dev jpeg-dev zlib-dev

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install --no-cache-dir psycopg2 \
    && apk del --no-cache .build-deps

# COPY Pipfile Pipfile.lock /opt/app/

COPY . /opt/app/

RUN pip install pipenv && pipenv install --dev --system

# COPY start.sh /start.sh

EXPOSE 8000

CMD ["/start.sh", "-docker"]
