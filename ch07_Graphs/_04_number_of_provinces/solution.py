from typing import List

class NumberOfProvincesSolution:
    def number_of_provinces(self, is_connected: List[List[int]]) -> int:
        visited = [False] * len(is_connected)
        count = 0
        for i in range(len(is_connected)):
            if not visited[i]:
                self._dfs(is_connected, visited, i)
                count += 1
        return count

    def _dfs(self, is_connected: List[List[int]], visited: List[bool], city: int) -> None:
        for other in range(len(is_connected)):
            if other != city and is_connected[city][other] == 1 and not visited[other]:
                visited[other] = True
                self._dfs(is_connected, visited, other)
