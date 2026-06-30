import pytest
from ch04_LinkedLists._00_linkedlist.node import Node
from ch04_LinkedLists._01_remove_dups.remove_dups import RemoveDups
from ch04_LinkedLists._01_remove_dups.solution import RemoveDupsSolution

@pytest.mark.parametrize("klass", [RemoveDups, RemoveDupsSolution])
def test_remove_dups(klass):
    instance = klass()
    try:
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(2)
        head.next.next.next = Node(3)
        head.next.next.next.next = Node(4)
        head.next.next.next.next.next = Node(1)

        instance.remove_dups(head)

        assert head.value == 1
        assert head.next.value == 2
        assert head.next.next.value == 3
        assert head.next.next.next.value == 4
        assert head.next.next.next.next is None
    except NotImplementedError:
        pytest.skip("RemoveDups is not implemented yet")
