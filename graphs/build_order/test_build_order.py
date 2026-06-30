import pytest
from graphs.build_order.build_order import BuildOrder
from graphs.build_order.solution import BuildOrderSolution

@pytest.mark.parametrize("klass", [BuildOrder, BuildOrderSolution])
def test_build_order(klass):
    instance = klass()
    try:
        projects = ["a", "b", "c", "d"]
        deps = [["a", "b"], ["a", "c"], ["a", "d"], ["c", "b"], ["d", "b"], ["d", "c"]]
        
        result = instance.build_order(projects, deps)
        assert result == ["a", "d", "c", "b"]

        # Cycle test
        cycle_deps = [["a", "b"], ["b", "c"], ["c", "d"], ["d", "a"]]
        with pytest.raises((ValueError, Exception)):
            instance.build_order(projects, cycle_deps)
    except NotImplementedError:
        pytest.skip("BuildOrder is not implemented yet")
