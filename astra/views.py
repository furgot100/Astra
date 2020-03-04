from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
import requests
from django.conf import settings
import json
from astra.models import Blog


# Create your views here.
class HomeView(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Astra"
        return context

def apod(request):
    apod_url="https://api.nasa.gov/planetary/apod"
    params = {
        'api_key' : settings.NASA_API_KEY
    }
    
    r = requests.get(apod_url, params=params)

    results = r.json()
    description = results["explanation"]
    title = results["title"]
    url = results["url"]

    return render(request, 'pages/apod.html', {
        'title' : title,
        'description': description,
        'url': url
    })

class BlogListView(ListView):
    """ Renders a list of all Pages. """
    model = Blog

    def get(self, request):
        """ GET a list of Pages. """
        blog = self.get_queryset().all()
        return render(request, 'list.html', {
          'blog': blog
        })