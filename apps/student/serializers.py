from rest_framework import serializers

from apps.group.serializers import GroupSerializer
from apps.student.models import Student


class StudentDetailSerializer(serializers.ModelSerializer):
    enrollments = GroupSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['dni', 'cui', 'name', 'last_name']
