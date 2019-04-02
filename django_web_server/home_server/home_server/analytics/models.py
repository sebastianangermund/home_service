import os

from django.db import models
import pandas as pd

from ..things.models import LedLight

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


class LedLightData(models.Model):
    """Model handling led light data

    """
    state_data = models.FileField(blank=True,
                                  upload_to='data_files/ledlights/')
    led_light = models.OneToOneField(LedLight, on_delete=models.CASCADE,
                                     related_name='ledlightdata')
    active = models.BooleanField(default=False)

    def __str__(self):
        return 'data for Led {}'.format(self.led_light)

    def write_data_point(self):
        state = self.ledlight.get_state
        path = 'data_files/ledlights/{}.csv'.format(self.pk)
        file = os.path.join(BASE_DIR, path)
        df_file = pd.read_csv(file, index=False)

        print('\n')
        print(state)    # write to csv here
        print('\n')
