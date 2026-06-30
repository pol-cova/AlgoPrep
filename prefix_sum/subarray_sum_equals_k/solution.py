from typing import List

class SubarraySumEqualsKSolution:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}
        prefix = 0
        count = 0

        for num in nums:
            prefix += num
            count += prefix_counts.get(prefix - k, 0)
            prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1

        return count
