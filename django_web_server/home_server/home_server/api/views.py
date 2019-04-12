from django.contrib.auth.models import User

from rest_framework.permissions import IsAdminUser
from rest_framework import (
    generics,
)

from ..things.models import LedLight
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


class ManagementCommands(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = LedLightStateSerializer
