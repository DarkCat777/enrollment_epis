from django.urls import path

from apps.course.views import CourseListCreateAPIView

urlpatterns = [
    path('', CourseListCreateAPIView.as_view()),
]
