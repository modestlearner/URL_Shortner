from django.conf.urls import url
from django.contrib import admin
from shortner.views import UrlRedirectView
from .views import wildcard_redirect

urlpatterns = [
    url(r'^(?P<path>.*)/', wildcard_redirect),
]