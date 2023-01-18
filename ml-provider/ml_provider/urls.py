from django.apps import apps
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.neural_network_parsing, name='neural_network'),
]