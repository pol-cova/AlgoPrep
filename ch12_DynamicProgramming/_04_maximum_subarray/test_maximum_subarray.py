import pytest
from ch12_DynamicProgramming._04_maximum_subarray.maximum_subarray import MaximumSubarray
from ch12_DynamicProgramming._04_maximum_subarray.solution import MaximumSubarraySolution

@pytest.mark.parametrize("klass", [MaximumSubarray, MaximumSubarraySolution])
def test_maximum_subarray(klass):
    instance = klass()
    try:
        assert instance.max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) == 6
        assert instance.max_sub_array([5,4,-1,7,8]) == 23
    except NotImplementedError:
        pytest.skip("MaximumSubarray is not implemented yet")
