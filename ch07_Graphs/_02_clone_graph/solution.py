from typing import Dict, Optional
from ch07_Graphs._02_clone_graph.clone_graph import Node

class CloneGraphSolution:
    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
        node_map = {}
        return self._clone(node, node_map)

    def _clone(self, node: Optional[Node], node_map: Dict[int, Node]) -> Optional[Node]:
        if node is None:
            return None

        if node.val in node_map:
            return node_map[node.val]

        new_node = Node(node.val)
        node_map[node.val] = new_node

        for neighbor in node.neighbors:
            new_node.neighbors.append(self._clone(neighbor, node_map))

        return new_node
