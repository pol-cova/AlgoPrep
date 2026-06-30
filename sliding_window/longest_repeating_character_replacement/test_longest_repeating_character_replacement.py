import pytest
from sliding_window.longest_repeating_character_replacement.longest_repeating_character_replacement import LongestRepeatingCharacterReplacement
from sliding_window.longest_repeating_character_replacement.solution import LongestRepeatingCharacterReplacementSolution

@pytest.mark.parametrize("klass", [LongestRepeatingCharacterReplacement, LongestRepeatingCharacterReplacementSolution])
def test_longest_repeating_character_replacement(klass):
    instance = klass()
    try:
        assert instance.character_replacement("ABAB", 2) == 4
        assert instance.character_replacement("AABABBA", 1) == 4
        assert instance.character_replacement("", 2) == 0
    except NotImplementedError:
        pytest.skip("LongestRepeatingCharacterReplacement is not implemented yet")
