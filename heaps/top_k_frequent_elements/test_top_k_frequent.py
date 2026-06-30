import pytest
from heaps.top_k_frequent_elements.top_k_frequent import TopKFrequent
from heaps.top_k_frequent_elements.solution import TopKFrequentSolution

@pytest.mark.parametrize("klass", [TopKFrequent, TopKFrequentSolution])
def test_top_k_frequent(klass):
    instance = klass()
    try:
        nums1 = [1, 1, 1, 2, 2, 3]
        assert sorted(instance.top_k_frequent(nums1, 2)) == [1, 2]

        nums2 = [1, 1, 2, 2, 3, 3, 3]
        assert instance.top_k_frequent(nums2, 1) == [3]
    except NotImplementedError:
        pytest.skip("TopKFrequent is not implemented yet")
