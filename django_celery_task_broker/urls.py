from django.conf.urls import url

from django_celery_task_broker.views.trigger_task_view import TriggerTaskView
from django_celery_task_broker.views.periodic_task_view import PeriodicTaskView
from django_celery_task_broker.views.crontab_schedule_view import CrontabScheduleView


urlpatterns = [
    url(r'^trigger-task/$', TriggerTaskView.as_view(), name='trigger_task'),
    url(r'^periodic-task/$', PeriodicTaskView.as_view(), name='periodic_task'),
    url(r'^crontab-schedule/$', CrontabScheduleView.as_view(), name='crontab_schedule')
]
