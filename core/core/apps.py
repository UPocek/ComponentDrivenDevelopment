import pkg_resources
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    provider_plugins = []
    visualizator_plugins = []

    def ready(self):
        self.provider_plugins = load_plugins("core.providers")
        self.visualizator_plugins = load_plugins("core.visualizators")

    def make_tree_view_node_dict(self, g, size):
        testGraph = g[size-1]
        nodes = testGraph.get_all_nodes()
        nodes_dict = {str(entry['id']):entry for entry in nodes.values()}
        for node in nodes:
            nodes_dict[str(node.id)]['neighbours'] = []
            for neighbour in node.get_all_neighbours().values():
                nodes_dict[str(node.id)]['neighbours'].append(neighbour)
        return nodes_dict

def load_plugins(group):
    plugins = []
    for entry_point in pkg_resources.iter_entry_points(group=group):
        plugin = entry_point.load()
        plugin = plugin()
        plugins.append(plugin)
    return plugins
    