import pytest
from graphs.number_of_islands.number_of_islands import NumberOfIslands
from graphs.number_of_islands.solution import NumberOfIslandsSolution

@pytest.mark.parametrize("klass", [NumberOfIslands, NumberOfIslandsSolution])
def test_number_of_islands(klass):
    instance = klass()
    try:
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        assert instance.num_islands(grid) == 3
        assert instance.num_islands([]) == 0
    except NotImplementedError:
        pytest.skip("NumberOfIslands is not implemented yet")
