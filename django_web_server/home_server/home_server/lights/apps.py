from django.apps import AppConfig


class LightsConfig(AppConfig):
    name = 'home_server.lights'
    verbose_name = "Lights"

    def ready(self):
        import home_server.lights.receivers
