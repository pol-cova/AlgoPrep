import pytest
from trees.binary_tree.node import Node
from trees.is_subtree.is_subtree import IsSubTree
from trees.is_subtree.solution import IsSubTreeSolution

@pytest.mark.parametrize("klass", [IsSubTree, IsSubTreeSolution])
def test_is_subtree(klass):
    instance = klass()
    try:
        first = Node(4)
        first.left = Node(5)
        first.right = Node(7)
        first.left.left = Node(1)
        first.left.right = Node(3)
        first.left.left.left = Node(8)

        # Non-subtree
        second_false = Node(4)
        second_false.left = Node(2)
        second_false.right = Node(7)
        second_false.left.left = Node(1)

        assert instance.is_subtree(first, second_false) is False

        # Subtree
        second_true = Node(5)
        second_true.left = Node(1)
        second_true.right = Node(3)
        second_true.left.left = Node(8)

        assert instance.is_subtree(first, second_true) is True
    except NotImplementedError:
        pytest.skip("IsSubTree is not implemented yet")
