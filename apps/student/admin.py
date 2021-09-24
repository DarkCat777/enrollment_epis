from django.contrib import admin

# Register your models here.
from apps.student.models import Student

admin.site.register(Student)
