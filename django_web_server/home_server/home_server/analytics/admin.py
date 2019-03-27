from django.contrib import admin

from .models import LedLightData


@admin.register(LedLightData)
class LedLightDataAdmin(admin.ModelAdmin):
    list_display = ['state_data']
