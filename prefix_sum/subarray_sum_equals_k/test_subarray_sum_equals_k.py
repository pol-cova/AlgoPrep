import pytest
from prefix_sum.subarray_sum_equals_k.subarray_sum_equals_k import SubarraySumEqualsK
from prefix_sum.subarray_sum_equals_k.solution import SubarraySumEqualsKSolution

@pytest.mark.parametrize("klass", [SubarraySumEqualsK, SubarraySumEqualsKSolution])
def test_subarray_sum_equals_k(klass):
    instance = klass()
    try:
        assert instance.subarray_sum([1, 1, 1], 2) == 2
        assert instance.subarray_sum([1, 2, 3], 3) == 2
        assert instance.subarray_sum([1, -1, 0], 0) == 3
    except NotImplementedError:
        pytest.skip("SubarraySumEqualsK is not implemented yet")
