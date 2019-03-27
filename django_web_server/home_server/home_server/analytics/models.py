import os

from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

import pandas as pd

from ..things.models import LedLight

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


class LedLightData(models.Model):
    """Model handling led light data

    """
    state_data = models.FileField(blank=True,
                                  upload_to='data_files/ledlights/')
    led_light = models.OneToOneField(LedLight, on_delete=models.CASCADE)

    def write_data_point(self):
        state = self.ledlight.get_state
        path = f'data_files/ledlights/{self.pk}.csv'
        file = os.path.join(BASE_DIR, path)
        df_file = pd.read_csv(file, index=False)

        print('\n')
        print(state)
        print('\n')


@receiver(post_delete, sender=LedLightData)
def submission_delete(sender, instance, **kwargs):
    instance.state_data.delete(False)


@receiver(post_save, sender=LedLightData)
def initialize_csv_file(instance, created, **kwargs):
    if created:
        raw_data = {
            'timestamp': [],
            'state': [],
        }
        path = f'data_files/ledlights/{instance.pk}.csv'
        file = pd.DataFrame(raw_data, columns=['timestamp', 'state'])
        file.to_csv(path)
        instance.state_data = os.path.join(BASE_DIR, path)
        instance.save()
