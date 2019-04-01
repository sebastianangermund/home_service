from redis import Redis
from rq_scheduler import Scheduler
from datetime import datetime

from .service import logging_service
from ..analytics.models import LedLightData


def write_led_light_data():
    queryset = LedLightData.objects.filter(active=True)
    logging_service(queryset)


# Get a scheduler for the "foo" queue
scheduler = Scheduler('led', connection=Redis())

scheduler.schedule(
    scheduled_time=datetime.utcnow(),
    func=write_led_light_data,
    args=None,
    kwargs=None,
    interval=5,
    repeat=None,
    meta=None,
)
