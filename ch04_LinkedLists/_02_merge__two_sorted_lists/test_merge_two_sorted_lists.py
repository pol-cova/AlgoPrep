import pytest
from ch04_LinkedLists._00_linkedlist.node import Node
from ch04_LinkedLists._02_merge__two_sorted_lists.merge_two_sorted_lists import MergeTwoSortedLists
from ch04_LinkedLists._02_merge__two_sorted_lists.solution import MergeTwoSortedListsSolution

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

@pytest.mark.parametrize("klass", [MergeTwoSortedLists, MergeTwoSortedListsSolution])
def test_merge_two_lists(klass):
    instance = klass()
    try:
        l1 = array_to_list([1, 2, 4])
        l2 = array_to_list([2, 3, 5])
        
        res = instance.merge_two_lists(l1, l2)
        assert list_to_array(res) == [1, 2, 2, 3, 4, 5]
    except NotImplementedError:
        pytest.skip("MergeTwoSortedLists is not implemented yet")
