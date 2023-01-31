import os

from django.apps.registry import apps
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .form import XmlParserUploadForm
from django.core.files.storage import FileSystemStorage

from core.models import Node, Graph
from django.urls import reverse


# Create your views here.

# Create your views here.


def handle_uploaded_file(file):
    with open("../xml_provider/xml_provider/uploaded_data/upload.xml", 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
        return


def parse_xml_doc(request):
    formxml = XmlParserUploadForm(request.POST, request.FILES)
    # graph_name = request.GET['graph-name']
    # graph_description = request.GET['graph-description']
    # xml_doc = request.GET['xml-docs']
    print("#########################")
    print(request.FILES)
    print("#########################")
    handle_uploaded_file(request.FILES['file_content'])
    provider_plugins = apps.get_app_config("core").provider_plugins
    for plugin in provider_plugins:
        if plugin.identifier() == "xml_provider":
            plugin.load("imeglupoRetardirano", "opsi", "upload.xml")
            print("Ima ga brapo")

    return HttpResponseRedirect(reverse("index"))


def index(request):

    if request.method == 'POST':
        form = XmlParserUploadForm(request.POST,  request.FILES)
        if(form.is_valid()):
            handle_uploaded_file(request.FILES['file_content'])
            provider_plugins = apps.get_app_config("core").provider_plugins
            for plugin in provider_plugins:
                if plugin.identifier() == "xml_provider":
                    plugin.load(request.POST['graph_name'], request.POST['graph_description'], "upload.xml")

        return HttpResponseRedirect(reverse("index"))
    else:
        print(os.getcwd())
        files = os.listdir("../xml_provider/xml_provider/data")
        options = [(file, file) for file in files]
        form = XmlParserUploadForm()
    return render(request, 'xml_provider/index.html', {'options': options, 'form': form})
