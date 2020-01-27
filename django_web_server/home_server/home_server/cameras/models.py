import uuid
import os

from datetime import datetime
from django.db import models
from django.urls import reverse
from django.core.files import File

from .services import request_get, take_picture

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


class Camera(models.Model):
    """Model for camera."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey('auth.User', related_name='cameras',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=False)
    address = models.CharField(max_length=64, null=True,
                               blank=True, default='')
    port_number = models.CharField(max_length=4, default='-')

    def __str__(self):
        return f'{self.title} ({self.address})'

    def take_picture(self):
        pass


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    uploaded = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE,
                               related_name='photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',
                              height_field=None,
                              width_field=None,
                              max_length=100,
                              null=True,
                              blank=True)
    owner = models.ForeignKey('auth.User', related_name='my_photos',
                              on_delete=models.CASCADE)
    take_new = models.BooleanField(default=True)

    class Meta:
        ordering = ['uploaded', 'camera']

    def __str__(self):
        return f'{self.camera} ({self.uploaded})'

    def save(self, *args, **kwargs):
        if not self.take_new:
            super(Photo, self).save(*args, **kwargs)
            return
        self.take_new = False
        utc_now = str(datetime.utcnow())
        photo_name = f'{utc_now}.jpg'
        try:
            taken = take_picture(self.camera.address, photo_name)
        except Exception:
            super(Photo, self).save(*args, **kwargs)
            return
        photo_name = f'assets/photos/{photo_name}'
        photo_path = os.path.join(BASE_DIR, photo_name)
        self.photo.save(photo_name, File(open(photo_path, 'rb')))
