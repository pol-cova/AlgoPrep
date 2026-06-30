from typing import List

class SortStackSolution:
    def sort(self, stack: List[int]) -> List[int]:
        sorted_stack = []
        while stack:
            element = stack.pop()
            while sorted_stack and element > sorted_stack[-1]:
                stack.append(sorted_stack.pop())
            sorted_stack.append(element)
        return sorted_stack
