"""Exact BountyBook test for dijkstra."""
from dijkstra import dijkstra, shortest_path

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"C": 2, "D": 5},
    "C": {"D": 1},
    "D": {}
}

distances, previous = dijkstra(graph, "A")

assert distances["A"] == 0
assert distances["B"] == 1, f"A->B: {distances['B']}"
assert distances["C"] == 3, f"A->B->C: {distances['C']}"
assert distances["D"] == 4, f"A->B->C->D: {distances['D']}"

path = shortest_path(previous, "A", "D")
assert path == ["A", "B", "C", "D"], f"path A->D: {path}"

path_bc = shortest_path(previous, "A", "C")
assert path_bc == ["A", "B", "C"], f"path A->C: {path_bc}"

graph2 = {"X": {"Y": 1}, "Y": {}, "Z": {}}
dist2, prev2 = dijkstra(graph2, "X")
assert dist2["Z"] == float('inf'), "unreachable node should be inf"
assert shortest_path(prev2, "X", "Z") is None, "path to unreachable should be None"

dist3, _ = dijkstra({"A": {}}, "A")
assert dist3["A"] == 0

print("ALL TESTS PASSED")