from django.template.loader import render_to_string
from core.models import Node,Graph
from operator import itemgetter

class SimpleVisualizator():
    def __init__(self):
        pass
    def identifier(self):
        return "Simple visualizator"

    def name(self):
        return "Simple visualizator"

    def show(self, g):
        nodes = g.get_all_nodes()
        edges = []
        for node in nodes:
            for neighbour in node.get_all_neighbours():
                edges.append({"source": node.id, "target": neighbour.id})
        list_nodes = [entry for entry in nodes.values()]
        name_indexer = dict((p['id'], i) for i, p in enumerate(list_nodes))
        list_edges = []
        for edge in edges:
            source = edge["source"]
            target = edge["target"]
            list_edges.append( {"source":name_indexer[source],"target":name_indexer[target]})
        content = {"nodes": list_nodes,
                  "edges":list_edges}
        return render_to_string("simple_visualizator/simple_visualizator.html",context=content)
