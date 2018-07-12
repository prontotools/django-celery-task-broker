from django.test import TestCase

from django_celery_task_broker.utils import is_task_exist


class UtilsTaskViewTest(TestCase):

    def test_is_task_exist_with_valid_task_should_return_true(self):
        module_name = 'project.celery'
        task_name = 'example_task'

        self.assertTrue(is_task_exist(module_name, task_name))

    def test_is_task_exist_with_valid_task_should_return_false(self):
        module_name = 'invalid.tasks'
        task_name = 'active_withheld_answer'

        self.assertFalse(is_task_exist(module_name, task_name))
