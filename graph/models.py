from django.db import models
from django.db.models import CASCADE


# Create your models here.


class Graph(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Node(models.Model):
    graph = models.ForeignKey(Graph, related_name='nodes', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.graph.name} - {self.name}'


class Edge(models.Model):
    graph = models.ForeignKey(Graph, related_name='edges', on_delete=CASCADE)
    from_node = models.ForeignKey(Node, related_name='out_edges', on_delete=models.CASCADE)
    to_node = models.ForeignKey(Node, related_name='in_edges', on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.from_node.name} -> {self.to_node.name} ({self.weight})"
