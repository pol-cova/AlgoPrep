import pytest
from ch14_ExtraProblems._02_word_break.word_break import WordBreak
from ch14_ExtraProblems._02_word_break.solution import WordBreakSolution

@pytest.mark.parametrize("klass", [WordBreak, WordBreakSolution])
def test_word_break(klass):
    instance = klass()
    try:
        assert instance.word_break("applepenapple", ["apple", "pen"]) is True
        assert instance.word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    except NotImplementedError:
        pytest.skip("WordBreak is not implemented yet")
