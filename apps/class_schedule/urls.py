from django.urls import path

from apps.class_schedule.views import ClassScheduleListCreateAPIView

urlpatterns = [
    path('', ClassScheduleListCreateAPIView.as_view()),
]
