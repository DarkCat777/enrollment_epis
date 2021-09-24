from django.contrib import admin

# Register your models here.
from apps.course.models import Course

admin.site.register(Course)
