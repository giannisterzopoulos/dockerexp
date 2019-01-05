#!/bin/bash

echo Starting Gunicorn.

cd $PROJECT_ROOT

if [ ! -f $PROJECT_ROOT/.build ]; then
  echo "Collecting and compiling statics"
  python manage.py collectstatic --noinput
  python manage.py migrate
  date > $PROJECT_ROOT/.build
fi

exec gunicorn foobar.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
