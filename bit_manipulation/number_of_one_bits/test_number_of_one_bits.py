import pytest
from bit_manipulation.number_of_one_bits.number_of_one_bits import NumberOfOneBits
from bit_manipulation.number_of_one_bits.solution import NumberOfOneBitsSolution

@pytest.mark.parametrize("klass", [NumberOfOneBits, NumberOfOneBitsSolution])
def test_number_of_one_bits(klass):
    instance = klass()
    try:
        assert instance.number_of_one_bits(3) == 2
        assert instance.number_of_one_bits(8) == 1
        assert instance.number_of_one_bits(-5) == 31
    except NotImplementedError:
        pytest.skip("NumberOfOneBits is not implemented yet")
