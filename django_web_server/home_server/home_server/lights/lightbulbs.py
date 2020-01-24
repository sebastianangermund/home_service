import uuid

from django.db import models
from django.urls import reverse

from .services import request_get


class LightBulb(models.Model):
    """Model for lightbulb status."""
    status = {
        "payload":"",
        "address":"status",
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey('auth.User', related_name='lightbulb',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=False)
    address = models.CharField(max_length=64, null=True,
                               blank=True, default='')
    port_number = models.CharField(max_length=4, default='-')
    state = models.CharField(max_length=1000,default='-')

    def __str__(self):
        if self.address:
            return f'{self.title} - {self.address}'
        else:
            return f'{self.title} * has no address *'

    def save(self, *args, **kwargs):
        if not self.address:
            super(LightBulb, self).save(*args, **kwargs)
        else:
            url = f'http://{self.address}/{self.status["address"]}'
            params = self.status["payload"]
            response = request_get(url, params)
            if response["status"] == 200:
                self.state = f'{response["content"]}'
                super(LightBulb, self).save(*args, **kwargs)
            else:
                raise Exception(f'{response}')


class LightBulbSettings(models.Model):
    """Model for lightbulb settings."""
    DEFAULT_STATE_CHOICES = (
        ('off', 'Off'),
        ('on', 'On'),
    )
    RESET = (
        (1, 'Reset'),
    )
    settings = {
        "payload":{
            "reset":"",
            "name":"",
            "ison":False,
            "has_timer":False,
            "default_state":"off",
            "btn_type":"toggle",
            "btn_reverse":0,
            "auto_on":0,
            "auto_off":0,
            "power":0,
            "btn_on_url":"",
            "btn_off_url":"",
            "out_on_url":"",
            "out_off_ulr":"",
            "longpush_url":"",
            "shortpush_url":"",
            "schedule":False,
            "schedule_rules":[],
        },
        "address":"settings/relay/0",
    }
    lightbulb = models.OneToOneField(LightBulb, on_delete=models.CASCADE,
                                     related_name='lightbulb_settings')
    reset = models.IntegerField(null=True, blank=True, choices=RESET)
    default_state = models.CharField(max_length=8,
                                     choices=DEFAULT_STATE_CHOICES,
                                     default='off')
    auto_off = models.IntegerField(null=True, blank=True, default=0)
    state = models.CharField(max_length=1000,default='-')
    schedule = models.BooleanField(default=False)
    schedule_rules = models.CharField(null=True, blank=True,
                                      max_length=1000, default='',
                                      help_text="Format: 0900-on,0930-off")

    def save(self, *args, **kwargs):
        if not self.lightbulb.address:
            super(LightBulbSettings, self).save(*args, **kwargs)
        else:
            url = f'http://{self.lightbulb.address}/{self.settings["address"]}'
            params = self.settings["payload"]
            params["default_state"] = self.default_state
            params["auto_off"] = self.auto_off
            params["name"] = self.lightbulb.title
            params["schedule"] = self.schedule
            rules = self.schedule_rules
            if rules:
                st = ''
                for el in rules.split(','):
                    st += el.split('-')[0] + '-0123456-' \
                        + el.split('-')[1] + ','
                params["schedule_rules"] = [st]
            response = request_get(url, params)
            if response["status"] == 200:
                self.state = response["content"]
                super(LightBulbSettings, self).save(*args, **kwargs)
                self.lightbulb.save()
            else:
                raise Exception(f'{response}')


class LightBulbRelay(models.Model):
    """Model for lightbulb relay."""
    SET_CHOICES = (
        ('off', 'Off'),
        ('on', 'On'),
        ('toggle', 'Toggle'),
    )
    relay = {
        "payload":{
            "turn":"off",
            "timer":0,
        },
        "address":"relay/0",
    }
    lightbulb = models.OneToOneField(LightBulb, on_delete=models.CASCADE,
                                     related_name='lightbulb_relay')
    set_state = models.CharField(max_length=8,
                                     choices=SET_CHOICES,
                                     default='off')
    timer = models.IntegerField(null=True, blank=True, default=0)
    state = models.CharField(max_length=1000,default='-')

    def save(self, *args, **kwargs):
        if not self.lightbulb.address:
            super(LightBulbRelay, self).save(*args, **kwargs)
        else:
            url = f'http://{self.lightbulb.address}/{self.relay["address"]}'
            params = self.relay["payload"]
            params["turn"] = self.set_state
            params["timer"] = self.timer
            response = request_get(url, params)
            if response["status"] == 200:
                self.state = response["content"]
                super(LightBulbRelay, self).save(*args, **kwargs)
                self.lightbulb.save()
            else:
                raise Exception(f'{response}')
