from django.apps import AppConfig


class PowerSwitchConfig(AppConfig):
    name = 'home_server.powerswitches'
    verbose_name = "PowerSwitch"

    def ready(self):
        import home_server.powerswitches.receivers
