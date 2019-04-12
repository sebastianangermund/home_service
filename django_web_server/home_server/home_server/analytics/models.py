import os

from datetime import datetime
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
        response = self.led_light.get_state()
        status = response.get('status')
        if type(status) is int and status == 200:
            content = response.get('content').decode("utf-8")
            state = 1 if content == 'ON' else 0
        elif type(status) is int:
            #   do something with status codes other than 200.
            state = '-'
        else:
            #   do something when no response is given
            state = '-'

        data = {
            'timestamp': [int(datetime.utcnow().timestamp())],
            'state': [state]
            }
        new_df_row = pd.DataFrame(data)
        database_file_path = 'data_files/ledlights/{}.csv'.format(self.pk)
        database_file = os.path.join(BASE_DIR, database_file_path)
        with open(database_file, 'a') as csv_file:
            (new_df_row).to_csv(csv_file, header=False)

        csv_file.close()
