import json
from django.apps.registry import apps
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from core.models import Node, Graph

visualizators = apps.get_app_config("core").visualizator_plugins
providers = apps.get_app_config("core").provider_plugins
context = {
'visualizators': visualizators,
'providers': providers
}

def index(request):
    if apps.get_app_config("core").original_graph is None and len(Graph.objects.all()) > 0:
        apps.get_app_config("core").original_graph = Graph.objects.all()[0]
    if apps.get_app_config("core").current_visualizator is None and len(apps.get_app_config("core").visualizator_plugins) > 0:
        apps.get_app_config("core").current_visualizator = apps.get_app_config("core").visualizator_plugins[0]
    context['all_graphs_from_db'] = Graph.objects.all()
    context['all_attributes'] = apps.get_app_config("core").get_all_attributes_of_selected_graph()    
    context['all_operators'] = apps.get_app_config("core").get_supported_operators()
    context['all_search_queries'] = apps.get_app_config("core").applied_searches
    context['all_filter_queries'] = apps.get_app_config("core").applied_filters
    context['tree_view'] = apps.get_app_config("core").make_tree_view_node_dict()
    context['bird_view'] = apps.get_app_config("core").make_bird_view()
    context['selected_graph'] = apps.get_app_config("core").get_graph_to_use()
    return render(request, 'core/index.html', context=context)

def choose_graph(request, graph_name):
    g = Graph.objects.get(name=graph_name)
    apps.get_app_config("core").original_graph = g
    delete_helper_graphs()
    apps.get_app_config("core").sub_graph = None
    apps.get_app_config("core").applied_searches.clear()
    apps.get_app_config("core").applied_filters.clear()
    return HttpResponseRedirect(reverse("index"))

@csrf_exempt
def filter_graph(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        search_content = body['search']
        filter_content = body['filter']
        
        if search_content.strip() != '':        
            apps.get_app_config("core").applied_searches.append(search_content)
        if filter_content['value'].strip() != '':
            apps.get_app_config("core").applied_filters.append(filter_content)
        if search_content.strip() != '' or filter_content['value'].strip() != '':
            delete_helper_graphs()
            new_graph_h = Graph(name = 'sub')
            new_graph_h.save()
            apps.get_app_config("core").apply(new_graph_h)
        return HttpResponseRedirect(reverse("index"))
    
def delete_search_query(request, query_id):
    apps.get_app_config("core").applied_searches.pop(query_id)
    delete_helper_graphs()
    new_graph = Graph(name = 'sub')
    new_graph.save()
    apps.get_app_config("core").apply(new_graph)
    return HttpResponseRedirect(reverse("index"))

def delete_filter_query(request, query_id):
    apps.get_app_config("core").applied_filters.pop(query_id)
    delete_helper_graphs()
    new_graph = Graph(name = 'sub')
    new_graph.save()
    apps.get_app_config("core").apply(new_graph)
    return HttpResponseRedirect(reverse("index"))
        

def load_visualizator(request,visualizator_name):
    visualizator_plugins = apps.get_app_config("core").visualizator_plugins
    for plugin in visualizator_plugins:
        if plugin.identifier() == visualizator_name:
            apps.get_app_config("core").current_visualizator = visualizator_name
            graph_to_visualise = apps.get_app_config("core").get_graph_to_use()
            if graph_to_visualise is not None:
                context['content'] = plugin.show(graph_to_visualise)
                return render(request, 'core/graph.html', context=context)

    return HttpResponse("None of visualizato plugins are installed or no graph selected")

def delete_helper_graphs():
    all_graphs_from_db = Graph.objects.all()
    for graph in all_graphs_from_db:
        if(graph.name == 'sub'):
            for node in graph.get_all_nodes():
                Node.objects.filter(pk=node.pk).delete()
            Graph.objects.filter(pk=graph.pk).delete()
