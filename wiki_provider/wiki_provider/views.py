from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.apps.registry import apps
from django.urls import reverse
import os
from core.models import Node, Graph


# Create your views here.
def scraping_form(request):
    return render(request, "wiki_provider/index.html")

def scrape_page(request):
    graph_name = request.GET['name']
    wiki_link = request.GET['wiki-link']
    depth = request.GET['depth']
    num_of_links = request.GET['num-of-links']

    provider_plugins = apps.get_app_config("core").provider_plugins
    for plugin in provider_plugins:
        if plugin.identifier() == "wiki_provider":
            plugin.load(graph_name=graph_name, wiki_link=wiki_link, depth=depth, num_of_links=num_of_links)
            break
    else:
        print("Nije instaliran plagin")
    return HttpResponseRedirect(reverse("index"))

