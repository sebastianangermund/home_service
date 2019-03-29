import uuid

from django.db import models
from django.urls import reverse

from .service import request_get
from ..settings import DEBUG


class LedLight(models.Model):
    """Model representing a led light.

    """
    INACTIVE = '-'
    OFF = '0'
    ON = '1'
    STATE_CHOICES = (
        (INACTIVE, 'inactive'),
        (OFF, 'off'),
        (ON, 'on')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey('auth.User', related_name='ledlight',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=False)
    address = models.CharField(max_length=64, null=True,
                               blank=True, default='')
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='-')

    class Meta:
        ordering = ['state', 'owner']

    def __str__(self):
        if self.address:
            return f'http://{self.address}:89/{self.id}'
        else:
            return f'{self.title} * has no address *'

    def get_absolute_url(self):
        return reverse('led-detail', args=[str(self.id)])

    def get_state(self):
        payload = 'http://127.0.0.1:89/id/state/' if DEBUG \
            else f'{self}/state/'

        return request_get(payload)

    def save(self, *args, **kwargs):
        if self.state == '-':
            super(LedLight, self).save(*args, **kwargs)
        else:
            payload = f'http://127.0.0.1:89/id/{self.state}/' if DEBUG \
                else f'{self}/{self.state}/'
            response = request_get(payload)

            print('\n')
            print(response)
            print('\n')

            if response.status_code == 200:
                super(LedLight, self).save(*args, **kwargs)
            elif type(response) == int:
                raise Exception(f'Status code {response} when making '
                                f'request {payload}')
            else:
                raise Exception(f'{response}')
