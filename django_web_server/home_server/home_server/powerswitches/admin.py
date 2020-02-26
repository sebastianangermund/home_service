from django.contrib import admin

from .models import (
    PowerSwitch,
    PowerSwitchSettings,
    PowerSwitchRelay,
)


@admin.register(PowerSwitch)
class PowerSwitchAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'state')
    list_filter = ('state', 'owner')

@admin.register(PowerSwitchSettings)
class PowerSwitchSettingsAdmin(admin.ModelAdmin):
    list_display = ('powerswitch', 'state', 'auto_off')
    list_filter = ('default_state', 'auto_off')

@admin.register(PowerSwitchRelay)
class PowerSwitchRelayAdmin(admin.ModelAdmin):
    list_display = ('powerswitch', 'state', 'timer')
    list_filter = ('set_state', 'timer')
