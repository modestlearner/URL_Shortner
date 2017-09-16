from __future__ import unicode_literals

from django.db import models
from shortner.models import URL
# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self , hjinstance):
        if isinstance(hjinstance,URL):
            obj , create = self.get_or_create(hj_url = hjinstance)
            obj.count +=1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    hj_url = models.ForeignKey(URL)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return self.count