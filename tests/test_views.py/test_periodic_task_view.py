import json

from django.urls import reverse

from django_celery_beat.models import CrontabSchedule, PeriodicTask
from rest_framework import status
from rest_framework.test import APITestCase

from django_celery_task_broker.utils import combine_task_path


class PeriodicTaskAPIViewTest(APITestCase):

    def setUp(self):
        self.company_account = 'http://gateway:8000/api/account/1000/'
        self.module_name = 'answers.tasks'
        self.task_name = 'active_withheld_answer'
        self.display_name = 'Test Dynamic Create Periodic Task'
        self.kwargs = {'company_account': self.company_account}
        self.url = reverse('periodic_task')
        self.schedule = CrontabSchedule.objects.create(
            minute='0',
            hour='3',
            day_of_week='*',
            day_of_month='*',
            month_of_year='*'
        )
        self.cron_id = self.schedule.id

        self.data = {
            'display_name': self.display_name,
            'cron_id': self.cron_id,
            'module_name': self.module_name,
            'task_name': self.task_name,
            'kwargs': self.kwargs
        }

    def test_post_view_when_task_already_exist_should_not_create_new_task_and_return_200_with_message(self):

        task_property = dict(
            crontab=self.schedule,
            name=self.display_name,
            task=combine_task_path(self.module_name, self.task_name),
            kwargs=json.dumps(self.kwargs)
        )
        PeriodicTask.objects.create(**task_property)

        actual = self.client.post(
            self.url,
            data=self.data,
            format='json'
        )

        self.assertEqual(actual.status_code, status.HTTP_200_OK)
        self.assertDictEqual(actual.json(), {'detail': f"Task:{task_property['task']} already exists"})
        self.assertEqual(PeriodicTask.objects.count(), 1)

    def test_post_view_should_create_periodic_task_and_return_status_200_with_message(self):
        message = 'CREATE: Test Dynamic Create Periodic Task: 0 3 * * * (m/h/d/dM/MY)'

        actual = self.client.post(
            self.url,
            data=self.data,
            format='json'
        )

        task = PeriodicTask.objects.last()

        self.assertEqual(task.crontab, self.schedule)
        self.assertEqual(task.name, self.display_name)
        self.assertEqual(task.task, combine_task_path(self.module_name, self.task_name))
        self.assertEqual(task.kwargs, json.dumps(self.kwargs))
        self.assertEqual(actual.status_code, status.HTTP_200_OK)
        self.assertDictEqual(actual.json(), {'detail': message})
