import pytest
from arrays_hashing.two_sum.two_sum import TwoSum
from arrays_hashing.two_sum.solution import TwoSumSolution

@pytest.mark.parametrize("klass", [TwoSum, TwoSumSolution])
def test_two_sum(klass):
    instance = klass()
    try:
        assert instance.two_sum([9, 2, 5, 6], 7) == [1, 2]
        assert instance.two_sum([9, 2, 5, 6], 100) is None
        assert instance.two_sum([3, 2, 4], 6) == [1, 2]
    except NotImplementedError:
        pytest.skip("TwoSum is not implemented yet")
