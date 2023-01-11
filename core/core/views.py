from django.apps.registry import apps
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Node, Graph
# Create your views here.

# This method is only for demonstration purposes
def test(request):
    g = Graph(name='Uki&Tasha graph')
    g.save()

    print(g.id)

    n = Node(atributes={'Uki':'cookie'})
    g.add_node(n) 

    n2 = g.create_and_add_node({'Tasha':'mali cookie'})
    n.add_neighbour(n2)
    print(g)

    for node in g.get_all_nodes():
        print(node)

    print(n.get_all_neighbours())

    n.add_atribute('malenic', "<3")

    print(n.get_atribute_value('malenic'))

    n.delete_atribute('malenic')

    print(n.delete_neighbour_by_id(3))

    n.delete_neighbour(n2)

    print(n.get_all_neighbours())

    return HttpResponse(g.id)

def index(request):
    visualizators = apps.get_app_config("core").visualizator_plugins
    print(visualizators)
    providers = apps.get_app_config("core").provider_plugins
    print(providers)
    context = {
        'visualizators': visualizators,
        'providers': providers
    }
    return render(request, 'core/index.html', context=context)

