# from .priorityqueue import PriorityQueue
# from .models import Node, Edge
#
#
# def dijkstrasalgorithm(graph_obj, start_node_id):
#     adjacency = {node.id: [] for node in graph_obj.nodes.all()}
#     for edge in graph_obj.edges.all():
#         adjacency[edge.from_node.id].append((edge.to_node.id, edge.weight))
#         adjacency[edge.to_node.id].append((edge.from_node.id, edge.weight))
#
#     distances = {node_id: float('inf') for node_id in adjacency}
#     distances[start_node_id] = 0
#     visited = set()
#
#     pq = PriorityQueue()
#     pq.push((0, start_node_id))
#
#     while len(pq) > 0:
#         current_dist, current_node = pq.pop()
#
#         if current_node in visited:
#             continue
#
#         visited.add(current_node)
#
#         for neighbor, weight in adjacency[current_node]:
#             distance = current_dist + weight
#
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 pq.push((distance, neighbor))
#
#     return distances




from .priorityqueue import PriorityQueue
from .models import Node, Edge


def dijkstrasalgorithm(graph_obj, start_node_name, end_node_name=None):
    # CHANGED: build adjacency using node names instead of IDs
    adjacency = {node.name: [] for node in graph_obj.nodes.all()}
    for edge in graph_obj.edges.all():
        adjacency[edge.from_node.name].append((edge.to_node.name, edge.weight))
        adjacency[edge.to_node.name].append((edge.from_node.name, edge.weight))

    # CHANGED: use node names for distances and previous_nodes
    distances = {name: float('inf') for name in adjacency}
    previous_nodes = {name: None for name in adjacency}
    distances[start_node_name] = 0
    visited = set()

    pq = PriorityQueue()
    pq.push((0, start_node_name))

    while len(pq) > 0:
        current_dist, current_node = pq.pop()

        if current_node in visited:
            continue
        visited.add(current_node)

        # CHANGED: early stop if we reached destination
        if end_node_name is not None and current_node == end_node_name:
            break

        for neighbor, weight in adjacency[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                pq.push((distance, neighbor))

    # CHANGED: reconstruct path using node names
    path = []
    if end_node_name is not None:
        current = end_node_name
        while current is not None:
            path.insert(0, current)
            current = previous_nodes[current]

    # CHANGED: return path and distances using node names
    return {
        "distances": distances,
        "path": path if end_node_name else None
    }
