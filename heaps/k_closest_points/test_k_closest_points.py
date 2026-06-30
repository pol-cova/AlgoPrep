import pytest
from heaps.k_closest_points.k_closest_points import KClosestPoints
from heaps.k_closest_points.solution import KClosestPointsSolution

@pytest.mark.parametrize("klass", [KClosestPoints, KClosestPointsSolution])
def test_k_closest_points(klass):
    instance = klass()
    try:
        assert instance.k_closest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
        assert sorted(instance.k_closest([[3, 3], [5, -1], [-2, 4]], 2)) == [[-2, 4], [3, 3]]
        assert instance.k_closest([], 3) == []
    except NotImplementedError:
        pytest.skip("KClosestPoints is not implemented yet")
