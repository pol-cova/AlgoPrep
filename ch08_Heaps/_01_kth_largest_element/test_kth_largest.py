import pytest
from ch08_Heaps._01_kth_largest_element.kth_largest import KthLargest
from ch08_Heaps._01_kth_largest_element.solution import KthLargestSolution

@pytest.mark.parametrize("klass", [KthLargest, KthLargestSolution])
def test_kth_largest(klass):
    try:
        kth = klass(4, [1, 2, 3, 4, 5])
        assert kth.add(6) == 3
        assert kth.add(1) == 3
        assert kth.add(8) == 4
    except NotImplementedError:
        pytest.skip("KthLargest is not implemented yet")
