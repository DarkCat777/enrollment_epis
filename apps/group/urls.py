from django.urls import path

from apps.group.views import CourseGroupListCreateAPIView

urlpatterns = [
    path('', CourseGroupListCreateAPIView.as_view()),
]
