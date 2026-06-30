from graphs.graph_search.graph_node_status import GraphNodeStatus

class GraphNode:
    def __init__(self, value: str):
        self.value = value
        self.status = GraphNodeStatus.Unvisited
        self.adjacents = {}

    def add_neighbor(self, node: 'GraphNode') -> None:
        if node.value not in self.adjacents:
            self.adjacents[node.value] = node
