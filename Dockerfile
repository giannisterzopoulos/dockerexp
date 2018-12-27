FROM python:3.4

ENV PROJECT_ROOT /opt/djangoapp/src

RUN mkdir -p /opt/djangoapp/src
WORKDIR /opt/djangoapp/src

COPY Pipfile Pipfile.lock /opt/djangoapp/src/
RUN pip install pipenv && pipenv install --dev --system

COPY .  /opt/djangoapp/src

COPY start.sh /start.sh

CMD ["/start.sh"]

EXPOSE 8000
