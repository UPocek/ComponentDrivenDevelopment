from django.apps import apps
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('xml_doc_parser', views.parse_xml_doc, name="parse_xml_doc")
]
