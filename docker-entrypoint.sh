#!/usr/bin/dumb-init /bin/sh

# Sleep for 10 seconds to wait for mysql to start completely
sleep 10
python manage.py migrate --noinput
#python manage.py initadmin
python manage.py runserver 0.0.0.0:9999
