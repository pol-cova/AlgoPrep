import pytest
from ch13_BitManipulation._01_number_of_one_bits.number_of_one_bits import NumberOfOneBits
from ch13_BitManipulation._01_number_of_one_bits.solution import NumberOfOneBitsSolution

@pytest.mark.parametrize("klass", [NumberOfOneBits, NumberOfOneBitsSolution])
def test_number_of_one_bits(klass):
    instance = klass()
    try:
        assert instance.number_of_one_bits(3) == 2
        assert instance.number_of_one_bits(8) == 1
        assert instance.number_of_one_bits(-5) == 31  # -5 has 31 set bits in 32-bit representation
    except NotImplementedError:
        pytest.skip("NumberOfOneBits is not implemented yet")
