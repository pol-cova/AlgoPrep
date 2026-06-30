from collections import deque
from ch07_Graphs._00_graph_search.graph import Graph
from ch07_Graphs._00_graph_search.graph_node import GraphNode
from ch07_Graphs._00_graph_search.graph_node_status import GraphNodeStatus

class RouteBetweenNodesSolution:
    def is_route_between(self, g: Graph, start: GraphNode, end: GraphNode) -> bool:
        if start == end:
            return True

        queue = deque([start])
        while queue:
            next_node = queue.popleft()
            if next_node == end:
                return True

            for neighbor in next_node.adjacents.values():
                if neighbor.status != GraphNodeStatus.Visited:
                    queue.append(neighbor)
                    neighbor.status = GraphNodeStatus.Visited

        return False
