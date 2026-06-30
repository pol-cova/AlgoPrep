from typing import List

class MaximumSubarraySolution:
    def max_sub_array(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if current_sum < 0:
                current_sum = 0
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)

        return max_sum
