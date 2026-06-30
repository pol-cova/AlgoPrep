from collections import deque
from ch07_Graphs._00_graph_search.graph import Graph
from ch07_Graphs._00_graph_search.graph_node import GraphNode
from ch07_Graphs._00_graph_search.graph_node_status import GraphNodeStatus

class BreadthFirstSearch:
    @staticmethod
    def breadth_first_search(graph: Graph, target: str) -> bool:
        for node in graph.nodes.values():
            if BreadthFirstSearch._single_bfs_helper(node, target):
                return True
        return False

    @staticmethod
    def _single_bfs_helper(node: GraphNode, target: str) -> bool:
        queue = deque([node])
        while queue:
            current_node = queue.popleft()
            if current_node.value == target:
                return True
            current_node.status = GraphNodeStatus.Visited
            for adj in current_node.adjacents.values():
                if adj.status == GraphNodeStatus.Unvisited:
                    queue.append(adj)
        return False
