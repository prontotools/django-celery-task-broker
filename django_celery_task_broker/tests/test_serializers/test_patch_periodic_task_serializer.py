from django.test import TestCase

from django_celery_task_broker.serializers import PatchPeriodicTaskSerializer


class PatchPeriodicTaskSerializerTest(TestCase):

    def setUp(self):
        self.company_account = 'http://gateway:8000/api/account/1000/'
        self.module_name = 'project.celery'
        self.task_name = 'example_task'
        self.kwargs = {'company_account': self.company_account}

        self.serializer = PatchPeriodicTaskSerializer

    def test_serializer_should_return_defined_fields(self):
        data = {
            'module_name': self.module_name,
            'task_name': self.task_name,
            'kwargs': self.kwargs,
            'enabled': True
        }
        serializer = self.serializer(data).data

        actual = {key for key in serializer.keys()}

        expected = {
            'module_name',
            'task_name',
            'kwargs',
            'enabled'
        }

        self.assertEqual(actual, expected)

    def test_serializer_should_require_all_required_field(self):
        data = {}
        expected_error = {
            'module_name': ['This field is required.'],
            'task_name': ['This field is required.'],
            'kwargs': ['This field is required.'],
            'enabled': ['This field is required.']
        }

        actual = self.serializer(data=data)

        self.assertFalse(actual.is_valid())
        self.assertDictEqual(actual.errors, expected_error)
