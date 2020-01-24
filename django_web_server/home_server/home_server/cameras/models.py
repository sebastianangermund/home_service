import uuid

from datetime import datetime
from django.db import models
from django.urls import reverse
from django.core.files import File

from .services import request_get, take_picture


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
                              null=True)
    owner = models.ForeignKey('auth.User', related_name='my_photos',
                              on_delete=models.CASCADE)
    take_new = models.BooleanField(default=False)

    class Meta:
        ordering = ['uploaded', 'camera']

    def __str__(self):
        return f'{self.camera} ({self.uploaded})'

    def save(self, *args, **kwargs):
        if not self.take_new:
            super(Photo, self).save(*args, **kwargs)
            return
        address = self.camera.address
        photo_path = take_picture(address)
        photo_name = f'{int(datetime.utcnow().timestamp())}.jpg'
        self.photo.save(photo_name, File(open(photo_path, 'rb')))
