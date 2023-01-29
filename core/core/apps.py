import pkg_resources
from django.apps import AppConfig
import operator


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    
    current_visualizator = None
    
    provider_plugins = []
    visualizator_plugins = []
    
    original_graph = None
    sub_graph = None
    applied_searches= []
    applied_filters= []

    def ready(self):
        self.provider_plugins = load_plugins("core.providers")
        self.visualizator_plugins = load_plugins("core.visualizators")
        
    def get_graph_to_use(self):
        return self.sub_graph if self.sub_graph is not None else self.original_graph
    
    def get_all_attributes_of_selected_graph(self):
        all_attributes = []
        if self.get_graph_to_use() is None:
            return all_attributes

        for node in self.get_graph_to_use().get_all_nodes():
            for attribute in node.get_all_atributes():
                if attribute not in all_attributes:
                    all_attributes.append(attribute)
        return all_attributes
    
    def apply(self, graph_holder):
        if len(self.applied_searches) == 0 and len(self.applied_filters) == 0:
            self.sub_graph = None
            return
        new_graph = self.copy_graph(self.original_graph, graph_holder)
        for search_reuqest in self.applied_searches:
            self.apply_search(new_graph, search_reuqest)
        for filter_request in self.applied_filters:
            self.apply_filter(new_graph, filter_request)
        self.sub_graph = new_graph
            
    def apply_search(self, new_graph, query):
        if new_graph is None:
            return
        id_of_nodes_that_do_not_fulfill_query = []
        for node in new_graph.get_all_nodes():
            if not self.node_fulfills_search_query(node, query):
                id_of_nodes_that_do_not_fulfill_query.append(node.id)
        for node in new_graph.get_all_nodes():
            for bad_node_id in id_of_nodes_that_do_not_fulfill_query:
                if bad_node_id in node.get_all_neighbour_ids():
                    node.delete_neighbour_by_id(bad_node_id)
        for node in new_graph.get_all_nodes():
            if node.id in id_of_nodes_that_do_not_fulfill_query:
                node.delete()
            
    
    def node_fulfills_search_query(self, node, query):
        for key, value in node.atributes.items():
            try:
                if query in key:
                    return True
            except Exception:
                pass
            try:
                if query in value:
                    return True
            except Exception:
                pass
            if(self.get_truth(query, operator.eq, value)):
                return True
        return False
    
    def apply_filter(self, new_graph,  query):
        if new_graph is None:
            return
        id_of_nodes_that_do_not_fulfill_query = []
        for node in new_graph.get_all_nodes():
            if not self.node_fulfills_filter_query(node, query):
                id_of_nodes_that_do_not_fulfill_query.append(node.id)
        for node in new_graph.get_all_nodes():
            for bad_node_id in id_of_nodes_that_do_not_fulfill_query:
                if bad_node_id in node.get_all_neighbour_ids():
                    node.delete_neighbour_by_id(bad_node_id)
        for node in new_graph.get_all_nodes():
            if node.id in id_of_nodes_that_do_not_fulfill_query:
                node.delete()
    
    def node_fulfills_filter_query(self, node, query):
        node_value = node.atributes[query['attribute']]
        query_value = query['value']
        if query['operator'] == '==':
            return self.get_truth(node_value , operator.eq, query_value)
        elif query['operator'] == '>':
            return self.get_truth(node_value, operator.gt, query_value)
        elif query['operator'] == '>=':
            return self.get_truth(node_value, operator.ge, query_value)
        elif query['operator'] == '<':
            return self.get_truth(node_value, operator.lt, query_value)
        elif query['operator'] == '<=':
            return self.get_truth(node_value, operator.le, query_value)
        elif query['operator'] == '!=':
            return self.get_truth(node_value, operator.ne, query_value)
    
    def get_truth(self, node_value, op, query_value):
        try:
            if op(node_value, str(query_value)):
                return True
        except Exception:
            pass
        try:
            if op(node_value, int(query_value)):
                return True
        except Exception:
            pass
        try:
            if op(node_value, float(query_value)):
                return True
        except Exception:
            pass
        return False
        
    def copy_graph(self, graph_to_copy, graph_new):
        visited_node_ids = {}
        for node in graph_to_copy.get_all_nodes():
            neighbours = node.get_all_neighbours()
            if node.id in visited_node_ids.keys():
                new_node = visited_node_ids[node.id]
            else:
                new_node = graph_new.create_and_add_node({key:value for (key,value) in node.atributes.items()})
                visited_node_ids[node.id] = new_node
            for neighbour in neighbours:
                if neighbour.id in visited_node_ids.keys():
                    new = visited_node_ids[neighbour.id]
                else:
                    new = graph_new.create_and_add_node({key:value for (key,value) in neighbour.atributes.items()})
                    visited_node_ids[neighbour.id] = new
                new_node.add_neighbour(new)
                            
        return graph_new
                    
    
    def get_supported_operators(self):
        if(self.get_graph_to_use() is None):
            return []
        return ['==', '>', '>=', '<', '<=', '!=']
            


def load_plugins(group):
    plugins = []
    for entry_point in pkg_resources.iter_entry_points(group=group):
        plugin = entry_point.load()
        plugin = plugin()
        plugins.append(plugin)
    return plugins
