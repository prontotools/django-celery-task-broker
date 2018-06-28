from importlib import import_module

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django_celery_task_broker.utils import is_task_exist
from django_celery_task_broker.serializers import TriggerTaskSerializer


class TriggerTaskView(APIView):

    def post(self, request):
        serializer = TriggerTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        if is_task_exist(data['module_name'], data['task_name']):
            module = import_module(data['module_name'])
            getattr(module, data['task_name']).apply_async(kwargs=data['kwargs'])
            return Response(data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail': 'Invalid Task'})
