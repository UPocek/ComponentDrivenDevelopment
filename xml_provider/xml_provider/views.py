import os

from django.apps.registry import apps
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from core.models import Node, Graph
from django.urls import reverse


# Create your views here.

# Create your views here.


def parse_xml_doc(request):
    graph_name = request.GET['graph-name']
    graph_description = request.GET['graph-description']
    xml_doc = request.GET['xml-docs']

    print(graph_name)
    print(graph_description)
    print(xml_doc)
    print("Nesto si uradio brato")

    provider_plugins = apps.get_app_config("core").provider_plugins
    for plugin in provider_plugins:
        if plugin.identifier() == "xml_provider":
            plugin.load(graph_name, graph_description, xml_doc)
            print("Ima ga brapo")

    return HttpResponseRedirect(reverse("index"))


def index(request):

    print(os.getcwd())
    files = os.listdir("../xml_provider/xml_provider/data")

    options = [(file, file) for file in files]
    print(options)
    return render(request, 'xml_provider/index.html', {'options':options})
