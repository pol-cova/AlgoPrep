import pytest
import copy
from arrays_hashing.zero_matrix.zero_matrix import ZeroMatrix
from arrays_hashing.zero_matrix.solution import ZeroMatrixSolution

@pytest.mark.parametrize("klass", [ZeroMatrix, ZeroMatrixSolution])
def test_zero_matrix(klass):
    instance = klass()
    try:
        matrix = [
            [2, 1, 3, 0, 2],
            [7, 4, 1, 3, 8],
            [4, 0, 1, 2, 1],
            [9, 3, 4, 1, 9]
        ]
        expected = [
            [0, 0, 0, 0, 0],
            [7, 0, 1, 0, 8],
            [0, 0, 0, 0, 0],
            [9, 0, 4, 0, 9]
        ]
        
        matrix_copy = copy.deepcopy(matrix)
        instance.zero_matrix(matrix_copy)
        assert matrix_copy == expected
    except NotImplementedError:
        pytest.skip("ZeroMatrix is not implemented yet")
