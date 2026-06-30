class ValidParenthesisSolution:
    def is_valid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ('(', '{', '['):
                stack.append(self._get_opposite(char))
            else:
                if not stack or stack.pop() != char:
                    return False
        return len(stack) == 0

    def _get_opposite(self, char: str) -> str:
        if char == '(': return ')'
        if char == '{': return '}'
        if char == '[': return ']'
        return '0'
