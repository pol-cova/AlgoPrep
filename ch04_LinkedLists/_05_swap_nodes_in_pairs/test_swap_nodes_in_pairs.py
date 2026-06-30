import pytest
from ch04_LinkedLists._00_linkedlist.node import Node
from ch04_LinkedLists._05_swap_nodes_in_pairs.swap_nodes_in_pairs import SwapNodesInPairs
from ch04_LinkedLists._05_swap_nodes_in_pairs.solution import SwapNodesInPairsSolution

def array_to_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for v in arr[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head

def list_to_array(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.value)
        curr = curr.next
    return arr

@pytest.mark.parametrize("klass", [SwapNodesInPairs, SwapNodesInPairsSolution])
def test_swap_nodes_in_pairs(klass):
    instance = klass()
    try:
        l1 = array_to_list([1, 2, 4, 6, 8])
        res = instance.swap_nodes_in_pairs(l1)
        assert list_to_array(res) == [2, 1, 6, 4, 8]
    except NotImplementedError:
        pytest.skip("SwapNodesInPairs is not implemented yet")
