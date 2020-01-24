from django.contrib import admin

from .models import (
    Camera,
    Photo,
)


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')
    list_filter = ('owner', 'port_number')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('uploaded', 'camera', 'owner')
    list_filter = ('uploaded', 'camera', 'owner')
