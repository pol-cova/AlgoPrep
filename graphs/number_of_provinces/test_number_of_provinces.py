import pytest
from graphs.number_of_provinces.number_of_provinces import NumberOfProvinces
from graphs.number_of_provinces.solution import NumberOfProvincesSolution

@pytest.mark.parametrize("klass", [NumberOfProvinces, NumberOfProvincesSolution])
def test_number_of_provinces(klass):
    instance = klass()
    try:
        matrix = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1]
        ]
        assert instance.number_of_provinces(matrix) == 2
        
        matrix2 = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        assert instance.number_of_provinces(matrix2) == 3
    except NotImplementedError:
        pytest.skip("NumberOfProvinces is not implemented yet")
