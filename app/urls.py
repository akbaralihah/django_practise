from django.urls import path
from app.views import UserGenericAPIView, student_courses

urlpatterns = [
    path("student-courses/", student_courses),
    path("users/", UserGenericAPIView.as_view(), name="user-list"),
]
