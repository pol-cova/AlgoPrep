import pytest
from ch06_Trees._00_binarytree.node import Node
from ch06_Trees._01_invert_binary_tree.invert_binary_tree import InvertBinaryTree
from ch06_Trees._01_invert_binary_tree.solution import InvertBinaryTreeSolution

@pytest.mark.parametrize("klass", [InvertBinaryTree, InvertBinaryTreeSolution])
def test_invert_tree(klass):
    instance = klass()
    try:
        root = Node(4)
        root.left = Node(2)
        root.right = Node(7)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(6)
        root.right.right = Node(9)

        inverted = instance.invert_tree(root)

        assert inverted.value == 4
        assert inverted.left.value == 7
        assert inverted.right.value == 2
        assert inverted.left.left.value == 9
        assert inverted.left.right.value == 6
        assert inverted.right.left.value == 3
        assert inverted.right.right.value == 1
    except NotImplementedError:
        pytest.skip("InvertBinaryTree is not implemented yet")
