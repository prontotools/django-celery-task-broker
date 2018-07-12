from __future__ import absolute_import
import os
from celery import Celery, shared_task

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

from celery import shared_task

@shared_task()
def example_task(first_arg, second_arg):
    print('Hello')
