import pytest
from arrays_hashing.group_anagrams.group_anagrams import GroupAnagrams
from arrays_hashing.group_anagrams.solution import GroupAnagramsSolution

@pytest.mark.parametrize("klass", [GroupAnagrams, GroupAnagramsSolution])
def test_group_anagrams(klass):
    instance = klass()
    try:
        words = ["saco", "arresto", "programa", "rastreo", "caso"]
        result = instance.group_anagrams(words)
        
        # Sort internal lists and the outer list to compare regardless of order
        sorted_result = sorted([sorted(group) for group in result])
        expected = sorted([sorted(["saco", "caso"]), sorted(["arresto", "rastreo"]), sorted(["programa"])])
        
        assert sorted_result == expected
    except NotImplementedError:
        pytest.skip("GroupAnagrams is not implemented yet")
