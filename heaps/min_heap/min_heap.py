class MinHeap:
    def __init__(self, size: int):
        self.max_size = size
        self.size = 0
        self.heap = [0] * size

    def _parent_index(self, i: int) -> int:
        return (i - 1) // 2

    def _left_child_index(self, i: int) -> int:
        return (i * 2) + 1

    def _right_child_index(self, i: int) -> int:
        return (i * 2) + 2

    def _is_leaf(self, i: int) -> bool:
        return self._right_child_index(i) >= self.size and self._left_child_index(i) >= self.size

    def insert(self, element: int) -> None:
        if self.size >= self.max_size:
            return
        self.heap[self.size] = element
        current = self.size
        while current > 0 and self.heap[current] < self.heap[self._parent_index(current)]:
            self._swap(current, self._parent_index(current))
            current = self._parent_index(current)
        self.size += 1

    def extract_min(self) -> int:
        if self.size <= 0:
            return -2147483648
        popped = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self._min_heapify(0)
        return popped

    def _min_heapify(self, i: int) -> None:
        if not self._is_leaf(i):
            left = self._left_child_index(i)
            right = self._right_child_index(i)

            smallest = i
            if left < self.size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < self.size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != i:
                self._swap(i, smallest)
                self._min_heapify(smallest)

    def _swap(self, x: int, y: int) -> None:
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]
