#1/bin/bash

python3 manage.py collectstatic --no-input

gunicorn Application.wsgi:application --bind 0.0.0.0:8000