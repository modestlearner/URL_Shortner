from django.conf.urls import url
from django.contrib import admin
from shortner.views import UrlRedirectView , Home

urlpatterns = [
    url(r'^$', Home.as_view(), name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<shortcode>[\w-]+)/$' , UrlRedirectView.as_view() , name="shortcodeurl"),


]
