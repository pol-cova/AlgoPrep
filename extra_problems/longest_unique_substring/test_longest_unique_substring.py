import pytest
from extra_problems.longest_unique_substring.longest_unique_substring import LongestUniqueSubstring
from extra_problems.longest_unique_substring.solution import LongestUniqueSubstringSolution

@pytest.mark.parametrize("klass", [LongestUniqueSubstring, LongestUniqueSubstringSolution])
def test_longest_unique_substring(klass):
    instance = klass()
    try:
        assert instance.length_of_longest_substring("aabcdefed") == 6
        assert instance.length_of_longest_substring("ccccc") == 1
    except NotImplementedError:
        pytest.skip("LongestUniqueSubstring is not implemented yet")
