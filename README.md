run virtual env:

    source djangoceleryenv/bin/activate

install modules:

    pip install -r requirements.txt

django:

    python manage.py makemigrations

    python manage.py migrate

redis:

    redis-server

celery:

    celery --app crm1.celery worker -l info

celery beat:

    celery -A crm1 beat -l info

Django Tutorial

    https://www.youtube.com/watch?v=3HPq12w-dww&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=22

Celery Tutorial:

    https://www.youtube.com/watch?v=EfWa6KH8nVI&list=PLLz6Bi1mIXhHKA1Szy2aj9Jbs6nw9fhNY
