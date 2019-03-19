import uuid

from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from ..service.service import communication


class LedLight(models.Model):
    """Model representing a led light.

    """
    ON = '1'
    OFF = '0'
    STATE_CHHOICES = (
        (ON, 'on'),
        (OFF, 'off')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey('auth.User', related_name='leds',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, default=None)
    state = models.CharField(max_length=1, choices=STATE_CHHOICES, default='0')

    class Meta:
        ordering = ['state', 'owner']

    def __str__(self):
        if self.address:
            return f'http://{self.address}:80/{self.id}'
        else:
            return self.title

    def get_absolute_url(self):
        return reverse('thing-detail', args=[str(self.id)])

    def get_state(self):
        payload = f'{self}/?state/'
        return communication(payload)

    def save(self, *args, **kwargs):
        payload = f'{self}/{self.state}/'
        print(payload)
        response = communication(payload)
        if response == 200:
            super(LedLight, self).save(*args, **kwargs)
        elif type(response) == int:
            raise Exception(f'Status code {response} when trying {self}')
        else:
            raise Exception(f'{response}')
