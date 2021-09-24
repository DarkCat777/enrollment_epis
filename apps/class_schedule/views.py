# Create your views here.
from rest_framework import generics

from apps.class_schedule.models import ClassSchedule
from apps.class_schedule.serializers import ClassScheduleSerializer


class ClassScheduleListCreateAPIView(generics.ListCreateAPIView):
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer
