from django.apps import AppConfig


class ThingsConfig(AppConfig):
    name = 'home_server.things'
    verbose_name = "Things"

    def ready(self):
        import home_server.things.receivers
