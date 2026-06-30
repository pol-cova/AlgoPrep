from typing import List

class GenerateParenthesisSolution:
    def generate_parenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []
        result = []
        self._generate_parenthesis(n, n, [], result)
        return result

    def _generate_parenthesis(self, open_left: int, close_left: int, current: List[str], result: List[str]) -> None:
        if open_left == 0 and close_left == 0:
            result.append("".join(current))
            return

        if open_left > 0:
            current.append('(')
            self._generate_parenthesis(open_left - 1, close_left, current, result)
            current.pop()

        if close_left > open_left:
            current.append(')')
            self._generate_parenthesis(open_left, close_left - 1, current, result)
            current.pop()
