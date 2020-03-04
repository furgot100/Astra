from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView, BlogListView
from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="home"), #home page?
    path("apod", views.apod, name="apod"),
    path("blog", BlogListView.as_view(), name="blog-list-view"),
]