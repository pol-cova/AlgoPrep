import pytest
from trees.binary_tree.node import Node
from trees.maximum_depth.maximum_depth import MaximumDepth
from trees.maximum_depth.solution import MaximumDepthSolution

@pytest.mark.parametrize("klass", [MaximumDepth, MaximumDepthSolution])
def test_maximum_depth(klass):
    instance = klass()
    try:
        root = Node(4)
        root.left = Node(2)
        root.right = Node(7)
        root.left.left = Node(1)
        
        assert instance.max_depth(root) == 3
        assert instance.max_depth(None) == 0
    except NotImplementedError:
        pytest.skip("MaximumDepth is not implemented yet")
