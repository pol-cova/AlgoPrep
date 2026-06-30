import pytest
from intervals.merge_intervals.merge_intervals import MergeIntervals
from intervals.merge_intervals.solution import MergeIntervalsSolution

@pytest.mark.parametrize("klass", [MergeIntervals, MergeIntervalsSolution])
def test_merge_intervals(klass):
    instance = klass()
    try:
        assert instance.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
        assert instance.merge([[1, 4], [4, 5]]) == [[1, 5]]
        assert instance.merge([]) == []
    except NotImplementedError:
        pytest.skip("MergeIntervals is not implemented yet")
