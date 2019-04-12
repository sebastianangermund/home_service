import uuid

from django.db import models
from django.urls import reverse

from .service import request_get
from ..settings import DEBUG


class LedLight(models.Model):
    """Model representing a led light.

    """
    mock = 'http://mock-service:9753'

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
    port_number = models.CharField(max_length=2, default='-')
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='-')

    class Meta:
        ordering = ['state', 'owner']

    def __str__(self):
        if self.address:
            return 'http://{}:{}/{}'.format(
                self.address, self.port_number, self.id)
        else:
            return '{} * has no address *'.format(self.title)

    def get_absolute_url(self):
        return reverse('led-detail', args=[str(self.id)])

    def get_state(self):
        """Queryd by both analytics and alarms.

        """
        payload = '{}/uuid/get-state/'.format(self.mock) if DEBUG \
            else '{}/get-state/'.format(self)

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
            payload = '{}/uuid/set-state={}/'.format(
                self.mock, self.state) if DEBUG \
                else '{}/set-state={}/'.format(self, self.state)
            print('\n')
            print('[*payload*]: ', payload)
            print('\n')
            response = request_get(payload)

            if response.status_code == 200:
                super(LedLight, self).save(*args, **kwargs)
            elif type(response) == int:
                raise Exception('Status code {} when making request {}'.format(
                    response, payload))
            else:
                raise Exception('{}'.format(response))
