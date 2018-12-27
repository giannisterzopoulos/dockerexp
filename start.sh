
echo Starting Gunicorn.

cd $PROJECT_ROOT

if [ ! -f $PROJECT_ROOT/.build ]; then
  echo "Collecting and compiling statics"
  pushd foobar
  python manage.py collectstatic --noinput
  popd
  date > $PROJECT_ROOT/.build
fi

cd foobar
exec gunicorn foobar.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
