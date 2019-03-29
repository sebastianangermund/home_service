import os

from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
import pandas as pd

from .models import LedLightData

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


def ready(self):
    # importing model classes
    LedLightData = self.get_model('LedLightData')

    # registering signals with the model's string label
    post_save.connect(initialize_csv_file, sender='app_label.LedLightData')


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

        print('\n')
        print(path)
        print('\n')

        file = pd.DataFrame(raw_data, columns=['timestamp', 'state'])
        file.to_csv(path)
        instance.state_data = os.path.join(BASE_DIR, path)
        instance.save()
    else:
        print('\n')
        print('NOT CREATED')
        print('\n')
