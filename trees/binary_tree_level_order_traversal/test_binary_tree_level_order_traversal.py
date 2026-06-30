import pytest
from trees.binary_tree.node import Node
from trees.binary_tree_level_order_traversal.binary_tree_level_order_traversal import BinaryTreeLevelOrderTraversal
from trees.binary_tree_level_order_traversal.solution import BinaryTreeLevelOrderTraversalSolution

@pytest.mark.parametrize("klass", [BinaryTreeLevelOrderTraversal, BinaryTreeLevelOrderTraversalSolution])
def test_binary_tree_level_order_traversal(klass):
    instance = klass()
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    try:
        assert instance.level_order(root) == [[3], [9, 20], [15, 7]]
        assert instance.level_order(None) == []
    except NotImplementedError:
        pytest.skip("BinaryTreeLevelOrderTraversal is not implemented yet")
