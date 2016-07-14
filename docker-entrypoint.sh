#!/usr/bin/env sh
set -e

# Check /data directory
chmod -R 700 $DB_DIR
chown -R guest $DB_DIR

# DEVELOPEMENT ENVIRONMENT
if [ "$1" = 'development' ]; then
  exec python3 manage.py runserver 0.0.0.0:8000
# PRODUCTION ENVIRONMENT
elif [ "$1" = 'production' ]; then
  export DEBUG=False
  exec uwsgi --ini uwsgi.ini --pythonpath $APP_DIR --static-map /static=$STATIC_ROOT
# TEST ENVIRONMENT
elif [ "$1" = 'test' ]; then
  export DEBUG=True
  exec uwsgi --ini uwsgi.ini --pythonpath $APP_DIR --static-map /static=$STATIC_ROOT
fi

exec "$@"
