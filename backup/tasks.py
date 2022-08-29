import pycron
from celery import shared_task
from datetime import datetime
from backup.models import Backup
import logging


logger = logging.getLogger(__name__)


@shared_task(queue='backup')
def backup():
    now = datetime.now()
    for b in Backup.objects.all():
        if pycron.is_now(b.crontab, now):
            logger.info(f'start backup of id: {b.id}')
            b.run_backup()
            logger.info(f'backup {b.id} has been done')
