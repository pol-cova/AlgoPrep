from typing import List

class SetSubsetsSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for element in nums:
            self._duplicate_subsets_adding_element(element, subsets)
        return subsets

    def _duplicate_subsets_adding_element(self, element: int, subsets: List[List[int]]) -> None:
        current_size = len(subsets)
        for i in range(current_size):
            new_subset = list(subsets[i])
            new_subset.append(element)
            subsets.append(new_subset)
