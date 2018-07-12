from django_celery_beat.models import CrontabSchedule
from rest_framework import serializers


class TriggerPeriodicTaskSerializer(serializers.Serializer):
    display_name = serializers.CharField(required=True)
    module_name = serializers.CharField(required=True)
    task_name = serializers.CharField(required=True)
    kwargs = serializers.JSONField(required=True)
    cron_id = serializers.CharField(required=True)


class PatchPeriodicTaskSerializer(serializers.Serializer):
    module_name = serializers.CharField(required=True)
    task_name = serializers.CharField(required=True)
    kwargs = serializers.JSONField(required=True)
    enabled = serializers.BooleanField(required=True)


class TriggerTaskSerializer(serializers.Serializer):
    module_name = serializers.CharField(required=True)
    task_name = serializers.CharField(required=True)
    kwargs = serializers.JSONField(required=True)


class CrontabScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrontabSchedule
        fields = '__all__'
