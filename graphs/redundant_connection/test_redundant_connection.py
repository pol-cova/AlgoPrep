import pytest
from graphs.redundant_connection.redundant_connection import RedundantConnection
from graphs.redundant_connection.solution import RedundantConnectionSolution

@pytest.mark.parametrize("klass", [RedundantConnection, RedundantConnectionSolution])
def test_redundant_connection(klass):
    instance = klass()
    try:
        edges1 = [[1, 2], [1, 3], [2, 3]]
        assert instance.find_redundant_connection(edges1) == [2, 3]

        edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        assert instance.find_redundant_connection(edges2) == [1, 4]
    except NotImplementedError:
        pytest.skip("RedundantConnection is not implemented yet")
