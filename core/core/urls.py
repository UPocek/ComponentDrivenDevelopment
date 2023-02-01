from django.apps import apps
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load_visualizator/<str:visualizator_name>', views.load_visualizator, name='load_visualizator'),
    path('choose_graph/<str:graph_name>', views.choose_graph, name='choose_graph'),
    path('filter', views.filter_graph, name='filter_graph'),
    path('delete_search_query/<int:query_id>', views.delete_search_query, name='delete_search_query'),
    path('delete_filter_query/<int:query_id>', views.delete_filter_query, name='delete_filter_query'),
    path('select_treeview_node', views.select_treeview_node)
]

provider_plugins = apps.get_app_config('core').provider_plugins

print([p.identifier() for p in provider_plugins])
for plugin in provider_plugins:
    plugin_path = path(f'{plugin.identifier()}/', include(f"{plugin.identifier()}.urls"))
    urlpatterns.append(plugin_path)

