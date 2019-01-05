
FROM python:3.4.9

ENV PROJECT_ROOT /opt/app

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY Pipfile Pipfile.lock /opt/app/

RUN pip install pipenv && pipenv install --dev --system

COPY . /opt/app/

COPY start.sh /start.sh

EXPOSE 8000

CMD ["/start.sh", "-docker"]
