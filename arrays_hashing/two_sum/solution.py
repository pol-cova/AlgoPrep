from typing import List, Optional

class TwoSumSolution:
    def two_sum(self, nums: List[int], target: int) -> Optional[List[int]]:
        if not nums or len(nums) <= 1:
            return None

        complement_map = {}
        for i, num in enumerate(nums):
            if num in complement_map:
                return [complement_map[num], i]
            complement = target - num
            complement_map[complement] = i
        return None
