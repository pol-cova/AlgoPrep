import pytest
import copy
from tries.word_search.word_search import WordSearch
from tries.word_search.solution import WordSearchSolution

@pytest.mark.parametrize("klass", [WordSearch, WordSearchSolution])
def test_word_search(klass):
    instance = klass()
    try:
        board = [
            ["p", "e", "r", "o"],
            ["a", "t", "a", "e"],
            ["t", "e", "l", "v"],
            ["o", "f", "l", "v"]
        ]
        words = ["pero", "pato", "comida", "veo", "pata"]
        
        board_copy = copy.deepcopy(board)
        result = instance.find_words(board_copy, words)
        
        assert sorted(result) == ["pata", "pato", "pero", "veo"]
    except NotImplementedError:
        pytest.skip("WordSearch is not implemented yet")
