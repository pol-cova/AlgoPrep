from graphs.graph_search.graph_node import GraphNode

class Graph:
    def __init__(self):
        self.nodes = {}

    def get_or_create_node(self, name: str) -> GraphNode:
        if name not in self.nodes:
            self.nodes[name] = GraphNode(name)
        return self.nodes[name]

    def add_edge(self, start: str, end: str) -> None:
        start_node = self.get_or_create_node(start)
        end_node = self.get_or_create_node(end)
        start_node.add_neighbor(end_node)
