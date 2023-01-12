from django.apps import apps
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.scraping_form, name='scraping_form'),
    path('scrape_page', views.scrape_page, name='scrape_page'),
]