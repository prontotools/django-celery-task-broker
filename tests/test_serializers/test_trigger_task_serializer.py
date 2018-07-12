from django.test import TestCase

from django_celery_task_broker.serializers import TriggerTaskSerializer


class TriggerTaskSerializerTest(TestCase):

    def setUp(self):
        self.company_account = 'http://gateway:8000/api/account/1000/'
        self.module_name = 'answers.tasks'
        self.task_name = 'active_withheld_answer'
        self.kwargs = {'company_account': self.company_account}

        self.serializer = TriggerTaskSerializer

    def test_serializer_should_return_defined_fields(self):
        data = {
            'module_name': self.module_name,
            'task_name': self.task_name,
            'kwargs': self.kwargs
        }
        serializer = self.serializer(data).data

        actual = {key for key in serializer.keys()}

        expected = {
            'module_name',
            'task_name',
            'kwargs'
        }

        self.assertEqual(actual, expected)

    def test_serializer_should_require_all_required_field(self):
        data = {}
        expected_error = {
            'module_name': ['This field is required.'],
            'task_name': ['This field is required.'],
            'kwargs': ['This field is required.']

        }

        actual = self.serializer(data=data)

        self.assertFalse(actual.is_valid())
        self.assertDictEqual(actual.errors, expected_error)
