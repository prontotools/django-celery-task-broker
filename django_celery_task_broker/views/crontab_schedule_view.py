from django_celery_beat.models import CrontabSchedule
from rest_framework.response import Response
from rest_framework.views import APIView

from django_celery_task_broker.serializers import CrontabScheduleSerializer


class CrontabScheduleView(APIView):

    def post(self, request):

        serializer = CrontabScheduleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=data['minute'],
            hour=data['hour'],
            day_of_week=data['day_of_week'],
            day_of_month=data['day_of_month'],
            month_of_year=data['month_of_year']
        )

        response_data = CrontabScheduleSerializer(crontab_schedule).data

        return Response(response_data)
