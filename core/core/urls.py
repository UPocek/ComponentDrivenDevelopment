from django.apps import apps
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('load_visualizator/<str:visualizator_name>', views.load_visualizator, name='load_visualizator'),
]
