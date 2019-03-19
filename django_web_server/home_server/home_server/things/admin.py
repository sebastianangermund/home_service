from django.contrib import admin

from .models import LedLight


@admin.register(LedLight)
class LedLightAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'id', 'state', 'owner')
    list_filter = ('state', 'owner')
