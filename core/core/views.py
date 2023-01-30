from django.apps.registry import apps
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Node, Graph
# Create your views here.

# This method is only for demonstration purposes

visualizators = apps.get_app_config("core").visualizator_plugins
providers = apps.get_app_config("core").provider_plugins
context = {
'visualizators': visualizators,
'providers': providers
}

def index(request):
    g = Graph.objects.all()
    size = len(Graph.objects.all())
    context['tree_view'] = apps.get_app_config("core").make_tree_view_node_dict(g, size)
    return render(request, 'core/tree_view.html', context=context)


def load_visualizator(request,visualizator_name):
    plugin_name = visualizator_name
    visualizator_plugins = apps.get_app_config("core").visualizator_plugins
    for plugin in visualizator_plugins:
        if plugin.identifier() == plugin_name:
            context['content'] = plugin.show()
            return render(request, 'core/graph.html', context=context)

    return HttpResponse("This plugin is not installed")
