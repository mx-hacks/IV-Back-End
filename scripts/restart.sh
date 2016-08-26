#!/bin/bash

HOME_DIR='/home/api/'
ENVIRONMENT_DIR='/home/api/environment'
PROJECT_DIR='/home/api/project'

cd $ENVIRONMENT_DIR
source vars.sh
source venv/bin/activate

cd $PROJECT_DIR
pip install -r requirements/prod.txt

python manage.py collectstatic --noinput

python manage.py migrate

service api restart
service nginx restart
