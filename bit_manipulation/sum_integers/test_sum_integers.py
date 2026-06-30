import pytest
from bit_manipulation.sum_integers.sum_integers import SumIntegers
from bit_manipulation.sum_integers.solution import SumIntegersSolution

@pytest.mark.parametrize("klass", [SumIntegers, SumIntegersSolution])
def test_sum_integers(klass):
    instance = klass()
    try:
        assert instance.get_sum(2, 5) == 7
        assert instance.get_sum(-2, 5) == 3
        assert instance.get_sum(-10, -20) == -30
    except NotImplementedError:
        pytest.skip("SumIntegers is not implemented yet")
