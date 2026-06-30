from typing import List

class QuickSortSolution:
    @staticmethod
    def sort(array: List[int]) -> None:
        QuickSortSolution._sort(array, 0, len(array) - 1)

    @staticmethod
    def _sort(array: List[int], low: int, high: int) -> None:
        if low < high:
            index = QuickSortSolution._partition(array, low, high)
            QuickSortSolution._sort(array, low, index - 1)
            QuickSortSolution._sort(array, index + 1, high)

    @staticmethod
    def _partition(array: List[int], low: int, high: int) -> int:
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
