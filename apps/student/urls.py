from django.urls import path

from apps.student.views import StudentListCreateAPIView, EnrollmentRetrieveAPIView

urlpatterns = [
    path('', StudentListCreateAPIView.as_view()),
    path('<int:pk>', StudentListCreateAPIView.as_view()),
    path('enrollment/<int:pk>', EnrollmentRetrieveAPIView.as_view()),
]
