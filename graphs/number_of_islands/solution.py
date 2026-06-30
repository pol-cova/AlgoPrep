from typing import List

class NumberOfIslandsSolution:
    def num_islands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        seen = set()
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in seen:
                    count += 1
                    self._dfs(grid, row, col, seen)

        return count

    def _dfs(self, grid: List[List[str]], row: int, col: int, seen: set) -> None:
        if (
            row < 0
            or col < 0
            or row >= len(grid)
            or col >= len(grid[0])
            or grid[row][col] != "1"
            or (row, col) in seen
        ):
            return

        seen.add((row, col))
        self._dfs(grid, row + 1, col, seen)
        self._dfs(grid, row - 1, col, seen)
        self._dfs(grid, row, col + 1, seen)
        self._dfs(grid, row, col - 1, seen)
