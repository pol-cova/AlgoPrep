import pytest
from graphs.clone_graph.clone_graph import Node, CloneGraph
from graphs.clone_graph.solution import CloneGraphSolution

@pytest.mark.parametrize("klass", [CloneGraph, CloneGraphSolution])
def test_clone_graph(klass):
    instance = klass()
    try:

        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n1.neighbors = [n2, n4]
        n2.neighbors = [n1, n3]
        n3.neighbors = [n2, n4]
        n4.neighbors = [n1, n3]

        cloned = instance.clone_graph(n1)

        assert cloned is not None
        assert cloned is not n1
        assert cloned.val == 1
        assert len(cloned.neighbors) == 2
        assert cloned.neighbors[0].val in (2, 4)
        assert cloned.neighbors[1].val in (2, 4)
        assert cloned.neighbors[0] is not n2
        assert cloned.neighbors[0] is not n4
    except NotImplementedError:
        pytest.skip("CloneGraph is not implemented yet")
