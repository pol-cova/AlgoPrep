import pytest
from searching.search_rotated_sorted_array.search_rotated_sorted_array import SearchRotatedSortedArray
from searching.search_rotated_sorted_array.solution import SearchRotatedSortedArraySolution

@pytest.mark.parametrize("klass", [SearchRotatedSortedArray, SearchRotatedSortedArraySolution])
def test_search_rotated_sorted_array(klass):
    instance = klass()
    try:
        assert instance.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
        assert instance.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
        assert instance.search([1], 1) == 0
    except NotImplementedError:
        pytest.skip("SearchRotatedSortedArray is not implemented yet")
