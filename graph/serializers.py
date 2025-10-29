from rest_framework import serializers
from .models import Graph , Node , Edge

class NodeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Node
        fields = ['id' , 'name' , 'graph']


class EdgeSerializer(serializers.ModelSerializer):
    from_node_name  = serializers.CharField(source="from_node.name" , read_only=True)
    to_node_name = serializers.CharField(source="to_node.name" , read_only=True)


    class Meta :
        model = Edge
        fields = ['id', 'from_node', 'to_node', 'from_node_name', 'to_node_name', 'weight', 'graph']
class GraphSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(many=True, read_only=True)
    edges = EdgeSerializer(many=True , read_only=True)


    class Meta :
        model = Graph
        fields = ['id' , 'name' , 'description' , 'nodes' , 'edges']