from .priorityqueue import PriorityQueue
from .models import Node, Edge


def dijkstrasalgorithm(graph_obj, start_node_id):
    adjacency = {node.id: [] for node in graph_obj.nodes.all()}
    for edge in graph_obj.edges.all():
        adjacency[edge.from_node.id].append((edge.to_node.id, edge.weight))
        adjacency[edge.to_node.id].append((edge.from_node.id, edge.weight))

    distances = {node_id: float('inf') for node_id in adjacency}
    distances[start_node_id] = 0
    visited = set()

    pq = PriorityQueue()
    pq.push((0, start_node_id))

    while len(pq) > 0:
        current_dist, current_node = pq.pop()

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in adjacency[current_node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                pq.push((distance, neighbor))

    return distances
