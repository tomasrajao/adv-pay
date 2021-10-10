release: python manage.py migrate
web: gunicorn advpay.wsgi --log-file -
worker: celery -A advpay worker -E -B --loglevel=DEBUG
