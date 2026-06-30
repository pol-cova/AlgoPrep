import pytest
from bit_manipulation.reverse_int.reverse_int import ReverseInt
from bit_manipulation.reverse_int.solution import ReverseIntSolution

@pytest.mark.parametrize("klass", [ReverseInt, ReverseIntSolution])
def test_reverse_int(klass):
    instance = klass()
    try:
        # Example 1: -5 in 32-bit signed -> reverse bits -> signed val is -536870913
        assert instance.reverse_bits(-5) == -536870913
        
        # Example 2: 43261596 -> reverse bits -> 964176192
        assert instance.reverse_bits(43261596) == 964176192
    except NotImplementedError:
        pytest.skip("ReverseInt is not implemented yet")
