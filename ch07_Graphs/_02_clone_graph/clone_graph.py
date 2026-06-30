from typing import List, Optional

class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class CloneGraph:
    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
        """
        Returns a deep copy (clone) of a connected, undirected graph.
        """
        raise NotImplementedError("Not implemented yet")
