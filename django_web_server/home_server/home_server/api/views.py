from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework import (
    generics, viewsets, permissions, parsers, decorators, response,
)

from ..lights.models import LedLight
from ..cameras.models import Camera, Photo
from ..services.service import write_led_light_data
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    LedLightSerializer, UserSerializer, LedLightStateSerializer,
    PhotoSerializer, PhotoFieldSerializer,
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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LedLightDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = LedLight.objects.all()
    serializer_class = LedLightSerializer


class LedLightState(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = LedLight.objects.all()
    serializer_class = LedLightStateSerializer


@api_view(['GET'])
def write_data_points(request, format=None):
    if request.method == 'GET':
        write_led_light_data()
        html = "<html><body>Done.</body></html>"
        return HttpResponse(html)


class PhotoViewSet(viewsets.ModelViewSet):
    """Generic view for API methods. Handles POST and GET automatically"""
    permission_classes = (
        # permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
        permissions.IsAdminUser,
    )
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @decorators.action(
        detail=True,
        methods=['PUT'],
        serializer_class=PhotoFieldSerializer,
        parser_classes=[parsers.MultiPartParser],
        permission_classes=[permissions.IsAdminUser],
    )
    def photo(self, request, pk):
        """Handles API PUT request for the "photo" instance to model "Photo"."""
        obj = self.get_object()
        serializer = self.serializer_class(
            obj,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST,
        )
