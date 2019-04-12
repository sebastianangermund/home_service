from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from rest_framework import (
    generics,
)

from ..things.models import LedLight
from ..services.service import write_led_light_data
from .serializers import (
    LedLightSerializer,
    UserSerializer,
    LedLightStateSerializer,
)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LedLightList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = LedLight.objects.all()
    serializer_class = LedLightSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LedLightDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = LedLight.objects.all()
    serializer_class = LedLightSerializer


class LedLightState(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = LedLight.objects.all()
    serializer_class = LedLightStateSerializer


@api_view(['GET'])
def write_data_points(request, format=None):
    """List all code snippets, or create a new snippet."""
    if request.method == 'GET':
        write_led_light_data()
        html = "<html><body>Done.</body></html>"
        return HttpResponse(html)
