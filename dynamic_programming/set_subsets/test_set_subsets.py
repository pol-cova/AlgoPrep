import pytest
from dynamic_programming.set_subsets.set_subsets import SetSubsets
from dynamic_programming.set_subsets.solution import SetSubsetsSolution

@pytest.mark.parametrize("klass", [SetSubsets, SetSubsetsSolution])
def test_set_subsets(klass):
    instance = klass()
    try:
        res = instance.subsets([1, 2, 3])
        sorted_res = sorted([sorted(subset) for subset in res])
        expected = sorted([[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]])
        assert sorted_res == expected
    except NotImplementedError:
        pytest.skip("SetSubsets is not implemented yet")
