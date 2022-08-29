import os

from celery import Celery
from celery.schedules import crontab
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_base.settings')

app = Celery(
    '_base',
    broker='amqp://{}:{}@{}/'.format(
        config('RABBITMQ_USER'),
        config('RABBITMQ_PASSWORD'),
        config('RABBITMQ_SERVER'),
    )
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'Backup': {
        'task': 'backup.tasks.backup.fill_ban_rules',
        'schedule': crontab(),
    },
}
