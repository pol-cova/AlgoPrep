class ClimbingStairsSolution:
    def climb_stairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev = 1
        current = 2

        for _ in range(3, n + 1):
            prev, current = current, prev + current

        return current
