from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm1.settings')

app = Celery('crm1')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Manila')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
  # # schedule by time
  # 'send-mail-every-day-at-8': {
  #   'task': 'send_mail_app.tasks.send_mail_func',
  #   'schedule': crontab(hour=16, minute=8),
  #   # 'args': (2,) # if needed args
  # }
  
  
  # peroidic task
  'backup-data-base-every-5-mins': {
    'task': 'aws_backup_and_restore.tasks.backup_aws_func',
    'schedule': 300.0, # by seconds
    # 'args': (2,) # if needed args
  }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
  print(f"Request: {self.request!r}")