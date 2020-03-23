from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.forms import User
# Create your models here.
class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages',on_delete=models.CASCADE)
    handle = models.TextField()
    message = models.TextField()
    #usuari = models.ForeignKey(User, related_name='propietari',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}
