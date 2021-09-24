from django.urls import path

from apps.student.views import StudentListCreateAPIView, EnrollmentListAPIView

urlpatterns = [
    path('', StudentListCreateAPIView.as_view()),
    path('<int:pk>', StudentListCreateAPIView.as_view()),
    path('enrollment', EnrollmentListAPIView.as_view()),
]
