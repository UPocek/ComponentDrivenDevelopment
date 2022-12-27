from django.db import models

# Create your models here.


class Graph(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    parent = models.ForeignKey("Graph", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Node(models.Model):
    name = models.CharField(max_length=100, null=False)
    data = models.TextField(null=False)
    graph = models.ForeignKey(Graph, null=False, on_delete=models.CASCADE, related_name="nodes")

    def __str__(self):
        return self.name


class Edge(models.Model):
    name = models.CharField(max_length=100, null=False)
    data = models.TextField(null=False)
    graph = models.ForeignKey(Graph, null=False, on_delete=models.CASCADE, related_name="edges")
    out = models.ForeignKey(Node, null=False, on_delete=models.CASCADE, related_name="out_edges")
    into = models.ForeignKey(Node, null=False, on_delete=models.CASCADE, related_name="in_edges")

    def __str__(self):
        return self.name
