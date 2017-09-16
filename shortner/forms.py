from django import forms
from .models import URL
from django.forms import ModelForm
from .validators import validate_url,validate_dot_com


class SubmitUrl(ModelForm):
    url = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Long URL" ,'class':"form-control" }))
    shortcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Type Short URL" ,'class':"form-control" }) , required=False)
    validators = [validate_url]
    class Meta:
        model = URL
        fields = ['url', 'shortcode']


