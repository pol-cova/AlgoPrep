import pytest
from searching.binary_search.binary_search import BinarySearch
from tries.title_suggestions.solution import Trie
from searching.binary_search.solution import BinarySearchSolution
from searching.binary_search.binary_search_iterative import BinarySearchIterative
from searching.binary_search.solution_iterative import BinarySearchIterativeSolution

@pytest.mark.parametrize("klass, name", [
    (BinarySearch, "BinarySearch"),
    (BinarySearchSolution, "BinarySearchSolution"),
    (BinarySearchIterative, "BinarySearchIterative"),
    (BinarySearchIterativeSolution, "BinarySearchIterativeSolution")
])
def test_binary_search(klass, name):
    instance = klass()
    array = [1, 3, 5, 7, 9, 11, 13, 15]
    try:
        assert instance.binary_search(array, 9) == 4
        assert instance.binary_search(array, 1) == 0
        assert instance.binary_search(array, 15) == 7
        assert instance.binary_search(array, 100) == -1
    except NotImplementedError:
        pytest.skip(f"{name} is not implemented yet")
