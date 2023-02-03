from core.services.Visualizators import Visualizator
from core.models import Node,Graph
from django.template.loader import render_to_string

class ArVisualizator(Visualizator):
    def __init__(self):
        pass

    def identifier(self):
        return "Ar visualizator"

    def name(self):
        return "Ar visualizator"

    def show(self, g):
        nodes = g.get_all_nodes()
        edges = []
        for node in nodes:
            for neighbour in node.get_all_neighbours():
                edges.append({"source": node.id, "target": neighbour.id})
        list_nodes = [entry for entry in nodes.values()]
        content = {"nodes": list_nodes,
                  "edges":edges}
        return render_to_string("ar_visualizator/ar_visualizator.html",context=content)
        
        
