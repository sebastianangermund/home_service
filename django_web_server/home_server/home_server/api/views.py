from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import (
    permissions,
    generics,
    status,
)

from ..things.models import LedLight
from .serializers import (
    LedLightSerializer,
    UserSerializer,
    LedLightOnOffSerializer,
)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LedLightList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)

    queryset = LedLight.objects.all()
    serializer_class = LedLightSerializer


class LedLightDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)

    queryset = LedLight.objects.all()
    serializer_class = LedLightSerializer


class LedLightOnOff(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)

    queryset = LedLight.objects.all()
    serializer_class = LedLightOnOffSerializer


@api_view(['PUT', 'GET'])
def led_on_off(request, pk, format=None):
    """Retrieve, update or delete a code snippet."""
    try:
        led = LedLight.objects.get(pk=pk)
    except LedLight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if led.owner == request.user or request.user.is_superuser:
        serializer = LedLightOnOffSerializer(led, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
