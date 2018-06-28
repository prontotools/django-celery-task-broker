import json

from django_celery_beat.models import CrontabSchedule, PeriodicTask
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django_celery_task_broker.serializers import TriggerPeriodicTaskSerializer
from django_celery_task_broker.utils import combine_task_path, is_task_exist


class PeriodicTaskView(APIView):

    def post(self, request):
        serializer = TriggerPeriodicTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        schedule = CrontabSchedule.objects.get(id=data['cron_id'])

        if is_task_exist(data['module_name'], data['task_name']):
            task_property = dict(
                crontab=schedule,
                name=data['display_name'],
                task=combine_task_path(data['module_name'], data['task_name']),
                kwargs=json.dumps(data['kwargs'])
            )
            if PeriodicTask.objects.filter(**task_property).exists():
                return Response(
                    status=status.HTTP_200_OK,
                    data={'detail': f"Task:{task_property['task']} already exists"}
                )
            task = PeriodicTask.objects.create(**task_property)
            return Response(status=status.HTTP_200_OK, data={'detail': f'CREATE: {str(task)}'})

        return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail': 'Invalid Task'})
