from typing import List

class BinarySearchSolution:
    def binary_search(self, array: List[int], target: int) -> int:
        return self._binary_search_helper(array, 0, len(array) - 1, target)

    def _binary_search_helper(self, array: List[int], left: int, right: int, target: int) -> int:
        if right >= left:
            mid = left + (right - left) // 2
            if array[mid] == target:
                return mid
            if array[mid] > target:
                return self._binary_search_helper(array, left, mid - 1, target)
            return self._binary_search_helper(array, mid + 1, right, target)
        return -1
