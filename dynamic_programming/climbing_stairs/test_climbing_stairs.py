import pytest
from dynamic_programming.climbing_stairs.climbing_stairs import ClimbingStairs
from dynamic_programming.climbing_stairs.solution import ClimbingStairsSolution

@pytest.mark.parametrize("klass", [ClimbingStairs, ClimbingStairsSolution])
def test_climbing_stairs(klass):
    instance = klass()
    try:
        assert instance.climb_stairs(2) == 2
        assert instance.climb_stairs(3) == 3
        assert instance.climb_stairs(5) == 8
    except NotImplementedError:
        pytest.skip("ClimbingStairs is not implemented yet")
