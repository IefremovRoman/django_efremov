web: gunicorn django_efremov.wsgi:application --log-level debug
worker: celery -A django_efremov worker --beat --concurrency 10 -l info