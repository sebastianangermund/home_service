from django.apps import AppConfig


class CameraConfig(AppConfig):
    name = 'home_server.cameras'
    verbose_name = "Cameras"

    # def ready(self):
    #     import home_server.cameras.receivers
