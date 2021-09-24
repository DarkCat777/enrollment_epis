from django.db import models

# Create your models here.
from apps.group.models import Group


class Student(models.Model):
    dni = models.IntegerField(null=False, blank=False)
    cui = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    enrollments = models.ManyToManyField(Group, blank=True)
