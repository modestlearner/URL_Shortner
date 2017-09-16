from __future__ import unicode_literals

from django.db import models
from .utils import create_shortcode
from django.conf import settings
from django_hosts.resolvers import reverse

SHORTCODE_MAX = getattr(settings , "SHORTCODE_MAX" , 15)
SHORTCODE_MIN = getattr(settings , "SHORTCODE_MIN" , 6)
# Create your models here.
class UrlManager(models.Manager):
    def all(self, *args ,**kwargs):
        qs_main = super(UrlManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active = True)
        return qs

    def refresh_shortcodes(self):
        qs = URL.objects.filter(id__gte = 1)
        new_code = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_code += 1
        return "New codes {}".format(new_code)


class URL(models.Model):
    url = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

    objects = UrlManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode=='':
            self.shortcode = create_shortcode(instance=self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(URL, self).save(*args, **kwargs)

    def __str__(self):
        return self.url

    # def get_absolute_url(self):
    #     return "http://www.hj.ml/{}".format(self.shortcode)

    def get_short_url(self):
        url_path = reverse("shortcodeurl",kwargs={'shortcode':self.shortcode} , host='www' , scheme='http')
        return url_path


