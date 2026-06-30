import heapq
from typing import List

class KClosestPointsSolution:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(heap, (distance, x, y))

        result = []
        for _ in range(min(k, len(heap))):
            _, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result
