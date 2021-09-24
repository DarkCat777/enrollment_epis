from django.db import models

# Create your models here.
from apps.course.models import Course


class Group(models.Model):
    name = models.CharField(max_length=128, null=False)
    classroom_no = models.IntegerField(null=False)
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE)
