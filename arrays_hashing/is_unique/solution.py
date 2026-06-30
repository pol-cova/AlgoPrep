class IsUniqueSolution:
    def is_unique(self, s: str) -> bool:
        # Assuming it is 128-character ASCII.
        if len(s) > 128:
            return False

        char_set = set()
        for char in s:
            if char in char_set:
                return False
            char_set.add(char)
        return True
