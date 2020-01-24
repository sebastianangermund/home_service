from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import LedLight
from ..analytics.models import LedLightData


def ready(self):
    # importing model classes
    LedLight = self.get_model('LedLight')

    # registering signals with the model's string label
    post_save.connect(initialize_analytics_instance,
                      sender='app_label.LedLight')


@receiver(post_save, sender=LedLight)
def initialize_analytics_instance(instance, created, **kwargs):
    if created:
        analytics_object = LedLightData(led_light=instance)
        analytics_object.save()

    if instance.state == '-':
        instance.ledlightdata.active = False
        instance.ledlightdata.save()
    else:
        instance.ledlightdata.active = True
        instance.ledlightdata.write_data_point()
        instance.ledlightdata.save()
