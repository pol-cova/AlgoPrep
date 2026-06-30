import pytest
from ch04_LinkedLists._00_linkedlist.node import Node
from ch04_LinkedLists._04_add_two_numbers.add_two_numbers import AddTwoNumbers
from ch04_LinkedLists._04_add_two_numbers.solution import AddTwoNumbersSolution

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

@pytest.mark.parametrize("klass", [AddTwoNumbers, AddTwoNumbersSolution])
def test_add_two_numbers(klass):
    instance = klass()
    try:
        l1 = array_to_list([1, 2, 4, 6])
        l2 = array_to_list([5, 2, 8])
        res = instance.add_two_numbers(l1, l2)
        assert list_to_array(res) == [6, 4, 2, 7]
    except NotImplementedError:
        pytest.skip("AddTwoNumbers is not implemented yet")
