from typing import List, Optional
from ch12_DynamicProgramming._01_robot_in_grid.cell import Cell

class RobotInGridSolution:
    def get_path(self, grid: List[List[bool]]) -> Optional[List[Cell]]:
        if not grid or not grid[0]:
            return None
        path = []
        # Copy the grid so we don't modify the input in-place during tests
        grid_copy = [row[:] for row in grid]
        if self._get_path(grid_copy, 0, 0, path):
            path.reverse()
            return path
        return None

    def _get_path(self, grid: List[List[bool]], row: int, col: int, path: List[Cell]) -> bool:
        if row >= len(grid) or col >= len(grid[0]) or not grid[row][col]:
            return False

        cell = Cell(row, col)
        is_at_finish = (row == len(grid) - 1) and (col == len(grid[0]) - 1)

        if is_at_finish or self._get_path(grid, row, col + 1, path) or self._get_path(grid, row + 1, col, path):
            path.append(cell)
            return True

        grid[row][col] = False
        return False
