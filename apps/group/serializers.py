from rest_framework import serializers

from apps.course.serializers import CourseSerializer
from apps.group.models import Group


class GroupDetailSerializer(serializers.ModelSerializer):
    id_course = CourseSerializer(many=False)

    class Meta:
        model = Group
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'classroom_no']
