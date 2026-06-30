from typing import List

class ZeroMatrixSolution:
    def zero_matrix(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        first_row_has_zero = any(val == 0 for val in matrix[0])
        first_col_has_zero = any(matrix[r][0] == 0 for r in range(len(matrix)))

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                self._set_row_to_zero(matrix, r)

        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                self._set_col_to_zero(matrix, c)

        if first_row_has_zero:
            self._set_row_to_zero(matrix, 0)
        if first_col_has_zero:
            self._set_col_to_zero(matrix, 0)

    def _set_row_to_zero(self, matrix: List[List[int]], row: int) -> None:
        for c in range(len(matrix[0])):
            matrix[row][c] = 0

    def _set_col_to_zero(self, matrix: List[List[int]], col: int) -> None:
        for r in range(len(matrix)):
            matrix[r][col] = 0
