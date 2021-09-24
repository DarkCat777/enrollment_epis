from rest_framework import serializers

from apps.class_schedule.models import ClassSchedule


class ClassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSchedule
        fields = ['start_time', 'end_time', 'day_of_week']
