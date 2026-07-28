"""MinHeap — array-based binary heap, no heapq. Supports push/pop/peek/heapify/len."""
from typing import List, Any


class MinHeap:
    def __init__(self):
        self._data: List[Any] = []

    def __len__(self) -> int:
        return len(self._data)

    def peek(self) -> Any:
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def push(self, value: Any) -> None:
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> Any:
        if not self._data:
            raise IndexError("pop from empty heap")
        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return top

    def heapify(self, values: List[Any]) -> None:
        """Replace contents with values, build heap in O(n) via Floyd."""
        self._data = list(values)
        # Start from last non-leaf and sift down
        for i in range((len(self._data) // 2) - 1, -1, -1):
            self._sift_down(i)

    def _sift_up(self, i: int) -> None:
        data = self._data
        while i > 0:
            parent = (i - 1) // 2
            if data[i] < data[parent]:
                data[i], data[parent] = data[parent], data[i]
                i = parent
            else:
                break

    def _sift_down(self, i: int) -> None:
        data = self._data
        n = len(data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and data[left] < data[smallest]:
                smallest = left
            if right < n and data[right] < data[smallest]:
                smallest = right
            if smallest == i:
                break
            data[i], data[smallest] = data[smallest], data[i]
            i = smallest