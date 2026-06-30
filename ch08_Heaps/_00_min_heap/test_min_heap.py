import pytest
from ch08_Heaps._00_min_heap.min_heap import MinHeap

def test_min_heap():
    min_heap = MinHeap(10)
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(17)
    min_heap.insert(10)
    min_heap.insert(84)
    min_heap.insert(19)
    min_heap.insert(6)
    min_heap.insert(22)
    min_heap.insert(9)

    assert min_heap.extract_min() == 3
    assert min_heap.extract_min() == 5
    assert min_heap.extract_min() == 6
