from core.services.Visualizators import Visualizator
from core.models import Node,Graph
from django.template.loader import render_to_string

class AdvencedVisualizator(Visualizator):
    def __init__(self):
        pass

    def identifier(self):
        return "Advanced visualizator"

    def name(self):
        return "Advanced visualizator"

    def show(self):
        all_graphs = Graph.objects.all()
        number_of_graphs = len(all_graphs)
        g = all_graphs[number_of_graphs-1]
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
        return render_to_string("advanced_visualizator/advanced_visualizator.html",context=content)
        
        
