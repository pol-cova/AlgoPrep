import pytest
from bit_manipulation.reverse_int.reverse_int import ReverseInt
from bit_manipulation.reverse_int.solution import ReverseIntSolution

@pytest.mark.parametrize("klass", [ReverseInt, ReverseIntSolution])
def test_reverse_int(klass):
    instance = klass()
    try:

        assert instance.reverse_bits(-5) == -536870913

        assert instance.reverse_bits(43261596) == 964176192
    except NotImplementedError:
        pytest.skip("ReverseInt is not implemented yet")
