"""Dijkstra's shortest path on a directed weighted graph.

graph: dict[node, dict[neighbor, weight]]
"""
import heapq
import math


def dijkstra(graph: dict, start):
    """Return (distances, previous) dicts. Unreachable nodes have distance = math.inf."""
    distances = {node: math.inf for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0

    # Heap of (distance, node)
    heap = [(0, start)]
    seen = set()

    while heap:
        d, node = heapq.heappop(heap)
        if node in seen:
            continue
        seen.add(node)
        for neighbor, weight in graph.get(node, {}).items():
            if neighbor in seen:
                continue
            new_d = d + weight
            if new_d < distances[neighbor]:
                distances[neighbor] = new_d
                previous[neighbor] = node
                heapq.heappush(heap, (new_d, neighbor))
    return distances, previous


def shortest_path(previous: dict, start, target):
    """Reconstruct path from start to target. Returns None if unreachable."""
    if target not in previous:
        return None
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = previous[cur]
    else:
        # Reached a node whose previous is None but it's not start → unreachable
        if path[-1] != start:
            return None
    path.reverse()
    return path