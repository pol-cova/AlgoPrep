from typing import List
from ch07_Graphs._00_graph_search.graph import Graph
from ch07_Graphs._00_graph_search.graph_node import GraphNode
from ch07_Graphs._00_graph_search.graph_node_status import GraphNodeStatus

class BuildOrderSolution:
    def build_order(self, projects: List[str], dependencies: List[List[str]]) -> List[str]:
        graph = self._build_dependency_graph(projects, dependencies)
        if graph is None:
            return list(projects)

        sorted_projects = []
        for node in graph.nodes.values():
            self._dfs(node, sorted_projects)

        sorted_projects.reverse()
        return sorted_projects

    def _dfs(self, node: GraphNode, ordered_projects: List[str]) -> None:
        if node.status == GraphNodeStatus.Unvisited:
            node.status = GraphNodeStatus.Visiting
            for adj in node.adjacents.values():
                self._dfs(adj, ordered_projects)
            node.status = GraphNodeStatus.Visited
            ordered_projects.append(node.value)
        elif node.status == GraphNodeStatus.Visiting:
            raise ValueError("Ciclo detectado")

    def _build_dependency_graph(self, projects: List[str], dependencies: List[List[str]]) -> Graph:
        if not dependencies:
            return None

        graph = Graph()
        for proj in projects:
            graph.get_or_create_node(proj)
        for dep in dependencies:
            graph.add_edge(dep[0], dep[1])
        return graph
