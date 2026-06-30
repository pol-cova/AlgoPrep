import pytest
from ch07_Graphs._00_graph_search.graph import Graph
from ch07_Graphs._01_route_between_nodes.route_between_nodes import RouteBetweenNodes
from ch07_Graphs._01_route_between_nodes.solution import RouteBetweenNodesSolution

@pytest.mark.parametrize("klass", [RouteBetweenNodes, RouteBetweenNodesSolution])
def test_route_between_nodes(klass):
    instance = klass()
    try:
        g = Graph()
        # Adjacency matrix from theory:
        # Node 0, 1, 2, 3, 4
        # Add edges:
        # 2 -> 1
        # 3 -> 2
        g.add_edge("2", "1")
        g.add_edge("3", "2")
        g.add_edge("4", "1")
        g.add_edge("4", "3")
        
        # Reset statuses just in case (though fresh graph starts Unvisited)
        n0 = g.get_or_create_node("0")
        n1 = g.get_or_create_node("1")
        n2 = g.get_or_create_node("2")
        n3 = g.get_or_create_node("3")
        n4 = g.get_or_create_node("4")
        
        # We need fresh graph/nodes for each test run because status is modified
        # So let's write helper inside test
        def build_fresh_graph():
            fresh = Graph()
            fresh.add_edge("2", "1")
            fresh.add_edge("3", "2")
            fresh.add_edge("4", "1")
            fresh.add_edge("4", "3")
            return fresh
            
        g = build_fresh_graph()
        assert instance.is_route_between(g, g.get_or_create_node("2"), g.get_or_create_node("4")) is False
        
        g = build_fresh_graph()
        assert instance.is_route_between(g, g.get_or_create_node("3"), g.get_or_create_node("1")) is True
        
        g = build_fresh_graph()
        assert instance.is_route_between(g, g.get_or_create_node("0"), g.get_or_create_node("1")) is False
        
        g = build_fresh_graph()
        assert instance.is_route_between(g, g.get_or_create_node("0"), g.get_or_create_node("0")) is True
    except NotImplementedError:
        pytest.skip("RouteBetweenNodes is not implemented yet")
