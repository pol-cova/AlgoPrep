import pytest
from stacks_queues.sort_stack.sort_stack import SortStack
from stacks_queues.sort_stack.solution import SortStackSolution

@pytest.mark.parametrize("klass", [SortStack, SortStackSolution])
def test_sort_stack(klass):
    instance = klass()
    try:
        stack = [1, 5, 2, 4]  # top is 4
        sorted_stack = instance.sort(stack)
        
        # The top of sorted_stack must be 1 (smallest element)
        assert sorted_stack.pop() == 1
        assert sorted_stack.pop() == 2
        assert sorted_stack.pop() == 4
        assert sorted_stack.pop() == 5
    except NotImplementedError:
        pytest.skip("SortStack is not implemented yet")
