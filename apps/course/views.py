# Create your views here.
from rest_framework import generics

from apps.course.models import Course
from apps.course.serializers import CourseSerializer


class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
