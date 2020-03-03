from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import requests

# Create your views here.
class HomeView(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Astra"
        return context

def apod(requests):
    nasa_url="https://api.nasa.gov/planetary/apod"
    