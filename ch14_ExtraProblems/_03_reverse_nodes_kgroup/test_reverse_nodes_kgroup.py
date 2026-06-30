import pytest
from ch14_ExtraProblems._03_reverse_nodes_kgroup.list_node import ListNode
from ch14_ExtraProblems._03_reverse_nodes_kgroup.reverse_nodes_kgroup import ReverseNodesKGroup
from ch14_ExtraProblems._03_reverse_nodes_kgroup.solution import ReverseNodesKGroupSolution

def array_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for v in arr[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def list_to_array(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr

@pytest.mark.parametrize("klass", [ReverseNodesKGroup, ReverseNodesKGroupSolution])
def test_reverse_nodes_kgroup(klass):
    instance = klass()
    try:
        # Example 1: k = 3
        l1 = array_to_list([1, 2, 3, 4, 5, 6, 7])
        res1 = instance.reverse_k_group(l1, 3)
        assert list_to_array(res1) == [3, 2, 1, 6, 5, 4, 7]

        # Example 2: k = 4
        l2 = array_to_list([1, 2, 3, 4, 5, 6, 7])
        res2 = instance.reverse_k_group(l2, 4)
        assert list_to_array(res2) == [4, 3, 2, 1, 5, 6, 7]
    except NotImplementedError:
        pytest.skip("ReverseNodesKGroup is not implemented yet")
