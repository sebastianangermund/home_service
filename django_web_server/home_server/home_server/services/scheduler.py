# from datetime import datetime
# from time import sleep
from background_task import background

from ..analytics.models import LedLightData
from .service import logging_service


@background()
def schedule_ledlight_logging():
    print('scheduler')
    queryset = LedLightData.objects.all()
    logging_service(queryset)


schedule_ledlight_logging(repeat=10)
