from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from apps.group.models import Group


class ClassSchedule(models.Model):
    class DayOfWeek(models.TextChoices):
        MONDAY = 'L', _('LUNES')
        TUESDAY = 'M', _('MARTES')
        WEDNESDAY = 'X', _('MIERCOLES')
        THURSDAY = 'J', _('JUEVES')
        FRIDAY = 'V', _('VIERNES')

    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    day_of_week = models.CharField(
        max_length=1,
        choices=DayOfWeek.choices,
        default=DayOfWeek.MONDAY,
    )

    id_group = models.ForeignKey(Group, on_delete=models.CASCADE)
