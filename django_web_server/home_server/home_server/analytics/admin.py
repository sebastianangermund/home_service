from django.contrib import admin

from .models import LedLightData


@admin.register(LedLightData)
class LedLightDataAdmin(admin.ModelAdmin):
    list_display = ('led_light', 'active', 'state_data')
    list_filter = ('led_light', 'active')
