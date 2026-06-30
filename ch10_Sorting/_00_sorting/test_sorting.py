import pytest
import copy
from ch10_Sorting._00_sorting.bubble_sort import BubbleSort
from ch10_Sorting._00_sorting.bubble_sort_solution import BubbleSortSolution
from ch10_Sorting._00_sorting.selection_sort import SelectionSort
from ch10_Sorting._00_sorting.selection_sort_solution import SelectionSortSolution
from ch10_Sorting._00_sorting.merge_sort import MergeSort
from ch10_Sorting._00_sorting.merge_sort_solution import MergeSortSolution
from ch10_Sorting._00_sorting.quick_sort import QuickSort
from ch10_Sorting._00_sorting.quick_sort_solution import QuickSortSolution

@pytest.mark.parametrize("klass, name", [
    (BubbleSort, "BubbleSort"),
    (BubbleSortSolution, "BubbleSortSolution"),
    (SelectionSort, "SelectionSort"),
    (SelectionSortSolution, "SelectionSortSolution"),
    (MergeSort, "MergeSort"),
    (MergeSortSolution, "MergeSortSolution"),
    (QuickSort, "QuickSort"),
    (QuickSortSolution, "QuickSortSolution"),
])
def test_sorting(klass, name):
    array = [8, 4, 0, 3, 6, 1, 7, 19, 12, 2]
    expected = [0, 1, 2, 3, 4, 6, 7, 8, 12, 19]
    
    array_copy = copy.deepcopy(array)
    try:
        klass.sort(array_copy)
        assert array_copy == expected
    except NotImplementedError:
        pytest.skip(f"{name} is not implemented yet")
