from django.test import TestCase

from django_celery_task_broker.serializers import TriggerPeriodicTaskSerializer


class TriggerPeriodicTaskSerializerTest(TestCase):

    def setUp(self):
        self.company_account = 'http://gateway:8000/api/account/1000/'
        self.module_name = 'answers.tasks'
        self.task_name = 'active_withheld_answer'
        self.cron_id = '1'
        self.display_name = 'Test Dynamic Create Periodic Task'
        self.kwargs = {'company_account': self.company_account}

        self.serializer = TriggerPeriodicTaskSerializer

    def test_serializer_should_return_defined_fields(self):
        data = {
            'module_name': self.module_name,
            'task_name': self.task_name,
            'display_name': self.display_name,
            'cron_id': self.cron_id,
            'kwargs': self.kwargs
        }
        serializer = self.serializer(data).data

        actual = {key for key in serializer.keys()}

        expected = {
            'display_name',
            'module_name',
            'task_name',
            'cron_id',
            'kwargs'
        }

        self.assertEqual(actual, expected)

    def test_serializer_should_require_all_required_field(self):
        data = {}
        expected_error = {
            'display_name': ['This field is required.'],
            'module_name': ['This field is required.'],
            'task_name': ['This field is required.'],
            'cron_id': ['This field is required.'],
            'kwargs': ['This field is required.']

        }

        actual = self.serializer(data=data)

        self.assertFalse(actual.is_valid())
        self.assertDictEqual(actual.errors, expected_error)
