from unittest.mock import patch

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class TriggerTaskViewAPIViewTest(APITestCase):

    def setUp(self):
        self.module_name = 'project.celery'
        self.task_name = 'example_task'
        self.company_account = 'http://gateway:8000/api/account/1000/'
        self.kwargs = {'company_account': self.company_account}
        self.url = reverse('trigger_task')

    def test_post_view_with_correct_task_should_trigger_task_correctly(self):
        data = {
            'module_name': self.module_name,
            'task_name': self.task_name,
            'kwargs': self.kwargs
        }
        with patch('project.celery.example_task.apply_async') as mock_task:
            self.client.post(path=self.url, data=data, format='json')

        mock_task.assert_called_once_with(kwargs=self.kwargs)

    def test_post_view_with_incorrect_task_should_return_bad_request(self):
        data = {
            'module_name': 'invalid-task-module',
            'task_name': self.task_name,
            'kwargs': self.kwargs
        }
        actual = self.client.post(path=self.url, data=data, format='json')

        self.assertEqual(actual.status_code, status.HTTP_400_BAD_REQUEST)
