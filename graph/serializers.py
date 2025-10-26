from rest_framework import serializers
from .models import Graph , Node , Edge

class NodeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Node
        fields = ['id' , 'name' , 'graph']


class EdgeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Edge
        fields = ['id' , 'from_node' , 'to_node' , 'weight' , 'graph']

class GraphSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(many=True, read_only=True)
    edges = EdgeSerializer(many=True , read_only=True)


    class Meta :
        model = Graph
        fields = ['id' , 'name' , 'description' , 'nodes' , 'edges']