from ch05_StacksQueues._00_stackqueue.node import Node
from ch05_StacksQueues._00_stackqueue.exceptions import MyEmptyStackException

class MyStack:
    def __init__(self):
        self.top = None

    def push(self, value: int) -> None:
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top

    def pop(self) -> int:
        if self.top is None:
            raise MyEmptyStackException()
        top_value = self.top.value
        self.top = self.top.next
        return top_value

    def peek(self) -> int:
        if self.top is None:
            raise MyEmptyStackException()
        return self.top.value

    def is_empty(self) -> bool:
        return self.top is None
