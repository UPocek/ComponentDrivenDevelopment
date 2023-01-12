
from django.template.loader import render_to_string


class SimpleVisualizator():
    def __init__(self):
        pass
    def identifier(self):
        return "Simple visualizator"

    def name(self):
        return "Simple visualizator"

    def show(self):
        print(render_to_string("simple_visualizator/simple_visualizator.html"));
        return render_to_string("simple_visualizator/simple_visualizator.html");
