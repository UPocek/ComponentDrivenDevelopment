from django.db import models
from picklefield.fields import PickledObjectField
# Create your models here.


class Graph(models.Model):
    name = models.CharField(max_length=50)

    def add_node(self, node):
        self.node_set.add(node, bulk=False)

    def create_and_add_node(self, atributes: dict):
        node = self.node_set.create(atributes=atributes)
        return node

    def get_all_nodes(self):
        return self.node_set.all()

    def __str__(self):
        output = "{name: " + self.name + ",\nnodes: ["
        for node in self.get_all_nodes():
            output += "\n" + str(node)
        output += "]\n}"
        return output


class Node(models.Model):
    atributes = PickledObjectField()
    neighbours = models.ManyToManyField('self', symmetrical=False, blank=True)
    graph = models.ForeignKey(Graph, on_delete=models.DO_NOTHING)

    def add_neighbour(self, node):
        self.neighbours.add(node)
        self.save()

    def delete_neighbour(self, node):
        self.neighbours.remove(node)
        self.save()
        
    def delete_neighbour_by_id(self, id):
        try:
            node_to_delete = self.neighbours.get(pk=id)
        except:
            return None
        self.neighbours.remove(node_to_delete)
        self.save()

    def get_all_neighbours(self):
        return self.neighbours.all()
    
    def get_all_neighbour_ids(self):
        ids = []
        for n in self.neighbours.all():
            ids.append(n.id)
        return ids

    def get_neighbour_count(self):
        return self.neighbours.count()

    def add_atribute(self, key, value):
        self.atributes[key] = value
        self.save()

    def delete_atribute(self, key):
        self.atributes.pop(key)
        self.save()

    def get_atribute_value(self, key):
        return self.atributes.get(key)
    
    def get_all_atributes(self):
        return self.atributes.keys()

    def __str__(self):
        return "{id: " + str(self.id) + ", atributes: " + str(self.atributes) + ", neighbours_count: " + str(self.get_neighbour_count()) + "}"
