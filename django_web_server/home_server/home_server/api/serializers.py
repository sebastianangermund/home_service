from rest_framework import serializers
from ..lights.models import LedLight
from ..cameras.models import Photo


from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=LedLight.objects.all()
    )
    class Meta:
        model = User
        fields = ('id', 'username', 'ledlight')


class LedLightSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = LedLight
        fields = ['title', 'owner', 'state', 'id', 'address']
        read_only_fields = ['owner', 'state', 'id']


class LedLightStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedLight
        fields = ['state']


class PhotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Photo
        fields = ['camera', 'photo', 'id', 'owner']
        read_only_fields = ['photo', 'owner', 'id']


class PhotoFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo']
