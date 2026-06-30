from stacks_queues.stack_queue.node import Node
from stacks_queues.stack_queue.exceptions import MyEmptyQueueException

class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, value: int) -> None:
        new_last = Node(value)
        if self.last is not None:
            self.last.next = new_last
        self.last = new_last
        if self.first is None:
            self.first = self.last

    def remove(self) -> int:
        if self.first is None:
            raise MyEmptyQueueException()
        first_value = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return first_value

    def peek(self) -> int:
        if self.first is None:
            raise MyEmptyQueueException()
        return self.first.value

    def is_empty(self) -> bool:
        return self.first is None
