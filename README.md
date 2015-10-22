# Celerydemo

[Celery](http://www.celeryproject.org/) is an asynchronous task queue/job queue based on distributed message passing.	It is focused on real-time operation, but supports scheduling as well.

This demo was built on Django, RabbitMQ, MySQL and Flower.

[Flower](https://github.com/mher/flower) is a Real-time monitor and web admin for Celery.

## Installation

Django, Celery, RabbitMQ, MySQL-python and Flower

## Structure
```
proj
├── manage.py
└── proj
    ├── __init__.py
    ├── settings.py
    └── ...
└── home
    ├── __init__.py
    ├── tasks.py
    └── ...
```

## Tests

```
# start django
$ python manage.py migrate
$ python manage.py runserver


#start rabbitmq server
$ rabbitmq-server

#start celery worker
$ celery -A proj worker -l debug
#start the celerybeat
$ celery -A proj beat -l debug --max-interval=10


# Flower: Launch the server and open [http://localhost:5555:](http://localhost:5555:)
#start celery
$ celery flower -A proj --broker=amqp://guest:guest@localhost:5672//

```

