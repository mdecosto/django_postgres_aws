run virtual env:

    source djangoceleryenv/bin/activate

install modules:

    pip install -r requirements.txt

django:

    python manage.py makemigrations

    python manage.py migrate

redis:

    redis-server

celery worker and beat:

    celery -A crm1 worker --beat --scheduler django --loglevel=info
