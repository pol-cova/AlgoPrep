class StackMinSolution:
    def __init__(self):
        self.values_stack = []
        self.min_stack = []

    def push(self, data: int) -> None:
        self.values_stack.append(data)
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self) -> int:
        if not self.values_stack:
            raise IndexError("Stack is empty")
        old_top = self.values_stack.pop()
        if old_top == self.min_stack[-1]:
            self.min_stack.pop()
        return old_top

    def min(self) -> int:
        if not self.min_stack:
            raise IndexError("Stack is empty")
        return self.min_stack[-1]
