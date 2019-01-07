
FROM python:3.4.9-alpine3.8

ENV PROJECT_ROOT /opt/app

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY . /opt/app/

# Install dependencies from Pipfile, making sure psycopg2 is
# successfully installed. Remove the extra packages in the end.
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    && pip install pipenv && pipenv install --dev --system \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

COPY start.sh /start.sh

EXPOSE 8000

CMD ["/start.sh", "-docker"]
