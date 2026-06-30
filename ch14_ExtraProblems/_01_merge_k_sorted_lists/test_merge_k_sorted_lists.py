import pytest
from ch14_ExtraProblems._01_merge_k_sorted_lists.node import Node
from ch14_ExtraProblems._01_merge_k_sorted_lists.merge_k_sorted_lists import MergeKSortedLists
from ch14_ExtraProblems._01_merge_k_sorted_lists.solution import MergeKSortedListsSolution

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

@pytest.mark.parametrize("klass", [MergeKSortedLists, MergeKSortedListsSolution])
def test_merge_k_sorted_lists(klass):
    instance = klass()
    try:
        l1 = array_to_list([1, 4, 5])
        l2 = array_to_list([1, 3, 4])
        l3 = array_to_list([2, 6])
        
        merged = instance.merge_k_lists([l1, l2, l3])
        assert list_to_array(merged) == [1, 1, 2, 3, 4, 4, 5, 6]
    except NotImplementedError:
        pytest.skip("MergeKSortedLists is not implemented yet")
