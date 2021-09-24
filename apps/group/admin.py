from django.contrib import admin

# Register your models here.
from apps.group.models import Group

admin.site.register(Group)