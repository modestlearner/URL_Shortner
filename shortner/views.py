from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , Http404
from django.views import View
from .models import URL
from .forms import SubmitUrl
from analytics.models import ClickEvent
from .utils import code_generator


# Create your views here.

class Home(View):
    form_class = SubmitUrl

    def get(self,request,*args,**kwargs):
        form=self.form_class(None)
        context = {
            "title":"localhost",
            "form": form,
        }
        return render(request, 'shortner/home.html',context )

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        print(request.POST)
        print(request.POST)
        context = {
            "title": "localhost",
            "form": form
        }
        template = 'shortner/home.html'
        if form.is_valid():
            print(form.cleaned_data)
            new_url = form.cleaned_data.get('url')
            new_shortcode = form.cleaned_data.get('shortcode')
            if new_shortcode=='':
                new_shortcode=code_generator()
            print(new_shortcode)
            object,create = URL.objects.get_or_create(url = new_url , shortcode = new_shortcode)
            context ={
                'object':object,
                'created':create,
            }
            if create:
                template = 'shortner/success.html'
            else:
                template = 'shortner/already_exists.html'

        return render(request, template,context)


class UrlRedirectView(View):
    def get(self , request, shortcode = None, *args , **kwargs):
        # print(shortcode
        # try:
        #     obj = URL.objects.get(shortcode=shortcode)
        # except:
        #     obj = URL.objects.all().first()
        # obj = get_object_or_404(URL, shortcode=shortcode)
        qs = URL.objects.filter(shortcode__iexact=shortcode)
        print(qs)
        if qs.count()!=1 and qs.exists():
            raise Http404
        obj = qs.first()
        print(obj)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)

    # def post(self , request, shortcode = None, *args , **kwargs):
