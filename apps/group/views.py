# Create your views here.
from rest_framework import generics

from apps.group.models import Group
from apps.group.serializers import GroupSerializer


class CourseGroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
