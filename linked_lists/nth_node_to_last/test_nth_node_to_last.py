import pytest
from linked_lists.linked_list.node import Node
from linked_lists.nth_node_to_last.nth_node_to_last import NthNodeToLast
from linked_lists.nth_node_to_last.solution import NthNodeToLastSolution

@pytest.mark.parametrize("klass", [NthNodeToLast, NthNodeToLastSolution])
def test_nth_node_to_last(klass):
    instance = klass()
    try:
        list_node = Node(1)
        list_node.next = Node(2)
        list_node.next.next = Node(4)
        list_node.next.next.next = Node(6)
        
        assert instance.nth_node_to_last(list_node, 1).value == 6
        assert instance.nth_node_to_last(list_node, 2).value == 4
        assert instance.nth_node_to_last(list_node, 3).value == 2
        assert instance.nth_node_to_last(list_node, 4).value == 1
        assert instance.nth_node_to_last(list_node, 5) is None
    except NotImplementedError:
        pytest.skip("NthNodeToLast is not implemented yet")
