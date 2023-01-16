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
        allGraphs = Graph.objects.all()
        numberOfGraphs = len(Graph.objects.all())
        if(numberOfGraphs > 0):
            g = allGraphs[numberOfGraphs-1]
            return render_to_string("advanced_visualizator/advanced_visualizator.html",context={'nodes': g.get_all_nodes()})
        
        
