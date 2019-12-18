import uuid

from django.db import models
from django.urls import reverse

from .service import request_get

DEBUG = False

class LedLight(models.Model):
    """Model representing a led light.

    """
    mock = 'http://192.168.1.11:9753'

    INACTIVE = '-'
    OFF = '0'
    ON = '1'
    BLINK = '2'
    STATE_CHOICES = (
        (INACTIVE, 'inactive'),
        (OFF, 'Off'),
        (ON, 'On'),
        (BLINK, 'blink')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey('auth.User', related_name='ledlight',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=False)
    address = models.CharField(max_length=64, null=True,
                               blank=True, default='')
    port_number = models.CharField(max_length=4, default='-')
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='-')

    class Meta:
        ordering = ['state', 'owner']

    def __str__(self):
        if self.address:
            return f'http://{self.address}:{self.port_number}/{self.id}'
        else:
            return f'{self.title} * has no address *'

    def get_absolute_url(self):
        return reverse('led-detail', args=[str(self.id)])

    def get_state(self):
        """Queryd by both analytics and alarms.

        """
        payload = f'{self.mock}/uuid/get-state/' if DEBUG \
            else f'{self}/get-state/'

        try:
            response = request_get(payload)
            return {
                'status': response.status_code,
                'encoding': response.encoding,
                'headers': response.headers,
                'content': response.content,
            }
        except:
            return {'status': 'No response'}

    def save(self, *args, **kwargs):
        if self.state == '-':
            super(LedLight, self).save(*args, **kwargs)
        else:
            payload = f'{self.mock}/uuid/set-state={self.state}/' if DEBUG \
                else f'{self}/set-state={self.state}/'

            response = request_get(payload)

            if response.status_code == 200:
                super(LedLight, self).save(*args, **kwargs)
            elif type(response) == int:
                raise Exception(
                    f'Status code {response} when making request {payload}'
                )
            else:
                raise Exception(f'{response}')
