from django.db.models import Value, F
from django.db.models.functions import Concat
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from app.serializers import UserSerializer
from app.models import StudentCouse


def student_courses(request):
    data = StudentCouse.objects.annotate(
        full_name=Concat(
            F("student__first_name"),
            Value(" "),
            F("student__last_name"),
        )
    ).values(
        "full_name",
        course_name=F("course__name"),
    )

    return JsonResponse(list(data), safe=False)


class UserGenericAPIView(ListModelMixin, GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.order_by("-date_joined")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)