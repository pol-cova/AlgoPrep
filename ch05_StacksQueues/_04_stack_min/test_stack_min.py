import pytest
from ch05_StacksQueues._04_stack_min.stack_min import StackMin
from ch05_StacksQueues._04_stack_min.solution import StackMinSolution

@pytest.mark.parametrize("klass", [StackMin, StackMinSolution])
def test_stack_min(klass):
    try:
        stack = klass()
        stack.push(3)
        stack.push(1)
        stack.push(2)
        
        assert stack.min() == 1
        stack.pop()
        assert stack.min() == 1
        stack.pop()
        assert stack.min() == 3
        stack.push(0)
        assert stack.min() == 0
    except NotImplementedError:
        pytest.skip("StackMin is not implemented yet")
