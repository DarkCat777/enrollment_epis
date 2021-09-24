from django.db import models


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=128, null=False)
    credit = models.IntegerField(null=False)
