from typing import List

class BinarySearchIterativeSolution:
    def binary_search(self, array: List[int], target: int) -> int:
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if array[mid] == target:
                return mid
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
