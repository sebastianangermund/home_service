from .service import logging_service
from ..analytics.models import LedLightData


def write_led_light_data():
    queryset = LedLightData.objects.filter(active=True)
    logging_service(queryset)
