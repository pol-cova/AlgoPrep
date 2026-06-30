import pytest
from ch13_BitManipulation._03_number_conversion.number_conversion import NumberConversion
from ch13_BitManipulation._03_number_conversion.solution import NumberConversionSolution

@pytest.mark.parametrize("klass", [NumberConversion, NumberConversionSolution])
def test_number_conversion(klass):
    instance = klass()
    try:
        assert instance.number_of_bits_to_flip_to_convert(5, 8) == 3
        assert instance.number_of_bits_to_flip_to_convert(0, 0) == 0
        assert instance.number_of_bits_to_flip_to_convert(-1, 0) == 32
    except NotImplementedError:
        pytest.skip("NumberConversion is not implemented yet")
