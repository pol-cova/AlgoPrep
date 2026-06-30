import pytest
from graphs.graph_search.graph import Graph
from graphs.route_between_nodes.route_between_nodes import RouteBetweenNodes
from graphs.route_between_nodes.solution import RouteBetweenNodesSolution

@pytest.mark.parametrize("klass", [RouteBetweenNodes, RouteBetweenNodesSolution])
def test_route_between_nodes(klass):
    instance = klass()
    try:
        g = Graph()

        g.add_edge("2", "1")
        g.add_edge("3", "2")
        g.add_edge("4", "1")
        g.add_edge("4", "3")

        n0 = g.get_or_create_node("0")
        n1 = g.get_or_create_node("1")
        n2 = g.get_or_create_node("2")
        n3 = g.get_or_create_node("3")
        n4 = g.get_or_create_node("4")

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
