#!/bin/sh

echo Starting Gunicorn.

cd $PROJECT_ROOT

#if [ ! -f $PROJECT_ROOT/.build ]; then
echo "Collecting and compiling statics"
python manage.py collectstatic --noinput
echo "Migrating default database"
python manage.py migrate --database=default
echo "Migrating specific database"
python manage.py migrate --database=specific
# date > $PROJECT_ROOT/.build
#fi

exec gunicorn foobar.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
