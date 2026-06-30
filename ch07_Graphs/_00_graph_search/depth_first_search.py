from ch07_Graphs._00_graph_search.graph import Graph
from ch07_Graphs._00_graph_search.graph_node import GraphNode
from ch07_Graphs._00_graph_search.graph_node_status import GraphNodeStatus

class DepthFirstSearch:
    @staticmethod
    def depth_first_search(graph: Graph, target: str) -> bool:
        for node in graph.nodes.values():
            if DepthFirstSearch._recursive_dfs_helper(node, target):
                return True
        return False

    @staticmethod
    def _recursive_dfs_helper(current_node: GraphNode, target: str) -> bool:
        if current_node.value == target:
            return True
        current_node.status = GraphNodeStatus.Visited
        for node in current_node.adjacents.values():
            if node.status != GraphNodeStatus.Visited:
                if DepthFirstSearch._recursive_dfs_helper(node, target):
                    return True
        return False
