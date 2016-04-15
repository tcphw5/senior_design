#!/bin/bash

NAME="Hanabi"                              #Name of the application (*)
DJANGODIR=/home/django/hanabi/             # Django project directory (*)
SOCKFILE=/home/django/hanabi/run/gunicorn.sock
USER=django                                        # the user to run as (*)
GROUP=www-data                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=senior_design.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=senior_design.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/django/venv/hanabi/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/django/venv/hanabi/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
