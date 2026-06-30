from typing import List, Set

class RedundantConnectionSolution:
    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        adj_list = [set() for _ in range(1001)]

        for edge in edges:
            first, second = edge[0], edge[1]
            if self._dfs(first, second, -1, adj_list):
                return edge
            else:
                adj_list[first].add(second)
                adj_list[second].add(first)
        return []

    def _dfs(self, first: int, second: int, previous: int, adj_list: List[Set[int]]) -> bool:
        if first == second:
            return True
        for w in adj_list[first]:
            if w == previous:
                continue
            if self._dfs(w, second, first, adj_list):
                return True
        return False
