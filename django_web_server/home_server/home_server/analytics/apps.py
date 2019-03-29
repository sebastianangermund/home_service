from django.apps import AppConfig


class AnalyticsConfig(AppConfig):
    name = 'home_server.analytics'
    verbose_name = "Analytics"

    def ready(self):
        import home_server.analytics.receivers
