import pytest
from stacks_queues.queue_with_stacks.queue_with_stacks import QueueWithStacks
from stacks_queues.queue_with_stacks.solution import QueueWithStacksSolution

@pytest.mark.parametrize("klass", [QueueWithStacks, QueueWithStacksSolution])
def test_queue_with_stacks(klass):
    try:
        queue = klass()
        assert queue.size() == 0
        queue.add(1)
        queue.add(2)
        queue.add(3)
        assert queue.remove() == 1
        assert queue.peek() == 2
        assert queue.size() == 2
        queue.add(4)
        assert queue.is_empty() is False
        assert queue.remove() == 2
        assert queue.remove() == 3
        assert queue.remove() == 4
        assert queue.is_empty() is True
    except NotImplementedError:
        pytest.skip("QueueWithStacks is not implemented yet")
