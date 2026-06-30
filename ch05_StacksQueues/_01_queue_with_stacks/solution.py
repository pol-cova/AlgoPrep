class QueueWithStacksSolution:
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def add(self, value: int) -> None:
        self.first_stack.append(value)

    def _shift_stacks(self) -> None:
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())

    def peek(self) -> int:
        self._shift_stacks()
        if not self.second_stack:
            raise IndexError("Queue is empty")
        return self.second_stack[-1]

    def remove(self) -> int:
        self._shift_stacks()
        if not self.second_stack:
            raise IndexError("Queue is empty")
        return self.second_stack.pop()

    def is_empty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return len(self.first_stack) + len(self.second_stack)
