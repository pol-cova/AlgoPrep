import pytest
import copy
from sorting.sorting_algorithms.bubble_sort import BubbleSort
from sorting.sorting_algorithms.bubble_sort_solution import BubbleSortSolution
from sorting.sorting_algorithms.selection_sort import SelectionSort
from sorting.sorting_algorithms.selection_sort_solution import SelectionSortSolution
from sorting.sorting_algorithms.merge_sort import MergeSort
from sorting.sorting_algorithms.merge_sort_solution import MergeSortSolution
from sorting.sorting_algorithms.quick_sort import QuickSort
from sorting.sorting_algorithms.quick_sort_solution import QuickSortSolution

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
