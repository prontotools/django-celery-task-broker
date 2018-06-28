from django.test import TestCase

from django_celery_beat.models import CrontabSchedule
from model_mommy import mommy

from django_celery_task_broker.serializers import CrontabScheduleSerializer


class ContrabScheduleSerializerTest(TestCase):

    def test_serializer_should_return_all_field(self):
        schedule = mommy.make(CrontabSchedule)
        serializer = CrontabScheduleSerializer(schedule).data

        actual = {key for key in serializer.keys()}

        expected = {
            'id',
            'minute',
            'hour',
            'day_of_week',
            'day_of_month',
            'month_of_year',
        }
        self.assertEqual(actual, expected)
