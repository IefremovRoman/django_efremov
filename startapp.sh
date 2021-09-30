#!/bin/bash

pip install -r $PWD/requirements.txt

flake8 django_efremov

python $PWD/manage.py makemigrations
python $PWD/manage.py migrate
# --run-syncdb

python $PWD/manage.py createsuperuser --noinput --user admin --email mail@mail.com

python $PWD/manage.py runserver