import pytest
from ch08_Heaps._03_relative_ranks.relative_ranks import RelativeRanks
from ch08_Heaps._03_relative_ranks.solution import RelativeRanksSolution

@pytest.mark.parametrize("klass", [RelativeRanks, RelativeRanksSolution])
def test_relative_ranks(klass):
    instance = klass()
    try:
        assert instance.find_relative_ranks([5, 4, 3, 2, 1]) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
        assert instance.find_relative_ranks([10, 3, 8, 9, 4]) == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
    except NotImplementedError:
        pytest.skip("RelativeRanks is not implemented yet")
