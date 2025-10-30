
from .priorityqueue import PriorityQueue
from .models import Node, Edge


def dijkstrasalgorithm(graph_obj, start_node_name, end_node_name=None):
    # CHANGED: build adjacency using node names instead of IDs
    adjacency = {node.name: [] for node in graph_obj.nodes.all()}
    for edge in graph_obj.edges.all():
        adjacency[edge.from_node.name].append((edge.to_node.name, edge.weight))
        adjacency[edge.to_node.name].append((edge.from_node.name, edge.weight))


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


        # if end_node_name is not None and current_node == end_node_name:
        #     break

        for neighbor, weight in adjacency[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                pq.push((distance, neighbor))


    all_paths= {}
    for node_name in adjacency:
        path = []
        current = node_name
        while current is not None:
            path.insert(0 , current)
            current = previous_nodes[current]
        all_paths[node_name] = path


    return {
        "distances": distances,
        "paths": all_paths
    }
