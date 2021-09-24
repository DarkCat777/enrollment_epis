# Create your views here.
from rest_framework import generics, serializers

from apps.class_schedule.models import ClassSchedule
from apps.class_schedule.serializers import ClassScheduleSerializer
from apps.course.serializers import CourseSerializer
from apps.group.models import Group
from apps.group.serializers import GroupSerializer
from apps.student.models import Student
from apps.student.serializers import StudentSerializer, StudentDetailSerializer


class StudentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentEnrollmentSerializer(serializers.BaseSerializer):

    def to_representation(self, instance: Student):
        groups = instance.enrollments.all()
        json = {'student': StudentDetailSerializer(instance).data}
        json_list = []
        for group in groups:
            json_list += [{
                'course': CourseSerializer(instance=group.id_course).data,
                'group': GroupSerializer(instance=group).data,
                'class_schedule': ClassScheduleSerializer(many=True,
                                                          instance=ClassSchedule.objects.filter(id_group=group.pk)).data
            }]
            print(json_list)
            json['courses'] = json_list
        return json


class EnrollmentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentEnrollmentSerializer
