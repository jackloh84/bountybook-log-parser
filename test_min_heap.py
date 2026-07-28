"""Exact BountyBook test for MinHeap."""
from min_heap import MinHeap

h = MinHeap()
assert len(h) == 0

h.push(5); h.push(2); h.push(8); h.push(1); h.push(4)
assert len(h) == 5
assert h.peek() == 1

results = [h.pop() for _ in range(5)]
assert results == [1, 2, 4, 5, 8], f"sorted order failed: {results}"
assert len(h) == 0

try:
    h.pop()
    assert False
except IndexError:
    pass

try:
    h.peek()
    assert False
except IndexError:
    pass

h2 = MinHeap()
h2.heapify([9, 3, 7, 1, 5, 2, 8])
assert len(h2) == 7
sorted_vals = [h2.pop() for _ in range(7)]
assert sorted_vals == [1, 2, 3, 5, 7, 8, 9], f"heapify sort failed: {sorted_vals}"

h3 = MinHeap()
h3.heapify([10, 20, 30])
h3.push(5)
assert h3.peek() == 5
assert h3.pop() == 5

h4 = MinHeap()
h4.push(42)
assert h4.peek() == 42
assert h4.pop() == 42
assert len(h4) == 0

print("ALL TESTS PASSED")