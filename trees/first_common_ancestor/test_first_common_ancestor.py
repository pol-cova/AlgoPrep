import pytest
from trees.binary_tree.node import Node
from trees.first_common_ancestor.first_common_ancestor import FirstCommonAncestor
from trees.first_common_ancestor.solution import FirstCommonAncestorSolution

@pytest.mark.parametrize("klass", [FirstCommonAncestor, FirstCommonAncestorSolution])
def test_first_common_ancestor(klass):
    instance = klass()
    try:
        root = Node(4)
        root.left = Node(5)
        root.right = Node(7)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.left.left.left = Node(8)

        assert instance.first_common_ancestor(root, root.left.left.left, root.right).value == 4
        assert instance.first_common_ancestor(root, root.left.left, root.left.right).value == 5
        assert instance.first_common_ancestor(root, root, root.right) is None
    except NotImplementedError:
        pytest.skip("FirstCommonAncestor is not implemented yet")
