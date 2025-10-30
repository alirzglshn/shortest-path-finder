from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view , action
from rest_framework import viewsets , status
from .models import Graph , Node , Edge
from .serializers import GraphSerializer , NodeSerializer , EdgeSerializer
from .algorithm import dijkstrasalgorithm

# Create your views here.


class GraphViewSet(viewsets.ModelViewSet):
    queryset = Graph.objects.all()
    serializer_class = GraphSerializer


    @action(detail=True, methods=['post'])
    def shortest_path(self, request, pk=None):
        graph = self.get_object()
        start_node_id = request.data.get('start_node_id')

        if not start_node_id:
            return Response({"error": "start_node_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Convert ID to node name
        try:
            start_node = graph.nodes.get(id=int(start_node_id))
        except Node.DoesNotExist:
            return Response({"error": f"Node {start_node_id} does not exist in this graph."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            # Pass node name to algorithm
            result = dijkstrasalgorithm(graph, start_node.name)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"Distances": result})


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class EdgeViewSet(viewsets.ModelViewSet):
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer





@api_view(['GET'])
def index(request):
    return Response({"message" : "hello world"})

