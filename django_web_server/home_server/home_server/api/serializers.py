from rest_framework import serializers
from ..things.models import LedLight


from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=LedLight.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'ledlight')


class LedLightSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LedLight
        fields = ['title', 'owner', 'state', 'id']
        read_only_fields = ['owner', 'state', 'id']


class LedLightOnOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedLight
        fields = ['state']
