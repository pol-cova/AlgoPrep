from typing import List
from collections import Counter
import heapq

class TopKFrequentSolution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # Using nlargest from heapq to get top K frequent elements
        return [item[0] for item in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
