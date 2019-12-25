from django.contrib import admin

from .models import LedLight, LightBulb, LightBulbSettings, LightBulbRelay


@admin.register(LedLight)
class LedLightAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'id', 'state')
    list_filter = ('state', 'owner')

@admin.register(LightBulb)
class LightBulbAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'id', 'state')
    list_filter = ('state', 'owner')

@admin.register(LightBulbSettings)
class LightBulbSettingsAdmin(admin.ModelAdmin):
    list_display = ('lightbulb', 'state', 'auto_off')
    list_filter = ('default_state', 'auto_off')

@admin.register(LightBulbRelay)
class LightBulbRelayAdmin(admin.ModelAdmin):
    list_display = ('lightbulb', 'state', 'timer')
    list_filter = ('set_state', 'timer')
