from django.urls import reverse

from django_celery_beat.models import CrontabSchedule
from rest_framework import status
from rest_framework.test import APITestCase


class CrontabScheduleAPIViewTest(APITestCase):

    def setUp(self):
        self.url = reverse('crontab_schedule')
        self.data = {
            'minute': '0',
            'hour': '3',
            'day_of_week': '*',
            'day_of_month': '*',
            'month_of_year': '*'
        }

    def test_post_view_when_crontab_schedule_exist_should_not_create_new_crontab_and_return_200_with_crontab(self):
        crontab_schedule = CrontabSchedule.objects.create(
            minute='0',
            hour='3',
            day_of_week='*',
            day_of_month='*'
        )

        actual = self.client.post(
            self.url,
            data=self.data,
            format='json'
        )

        self.assertEqual(actual.status_code, status.HTTP_200_OK)
        self.assertEqual(actual.json()['id'], crontab_schedule.id)
        self.assertEqual(CrontabSchedule.objects.count(), 1)

    def test_post_view_should_create_crontab_schedule_and_return_status_200_with_crontab(self):

        actual = self.client.post(
            self.url,
            data=self.data,
            format='json'
        )

        self.assertEqual(actual.status_code, status.HTTP_200_OK)
        self.assertEqual(actual.json()['minute'], '0')
        self.assertEqual(actual.json()['hour'], '3')
        self.assertEqual(actual.json()['day_of_week'], '*')
        self.assertEqual(actual.json()['day_of_month'], '*')
        self.assertEqual(actual.json()['month_of_year'], '*')
        self.assertEqual(CrontabSchedule.objects.count(), 1)
