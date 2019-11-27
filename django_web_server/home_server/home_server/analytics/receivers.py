import os

from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save

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
        data = f'timestamp: -, state: -'
        database_file_path = f'data_files/ledlights/{instance.pk}.csv'
        database_file = os.path.join(BASE_DIR, database_file_path)
        f = open(database_file, 'w+')
        f.write(data)
        f.close()
