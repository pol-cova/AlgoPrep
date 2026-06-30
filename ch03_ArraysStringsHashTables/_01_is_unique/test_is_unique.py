import pytest
from ch03_ArraysStringsHashTables._01_is_unique.is_unique import IsUnique
from ch03_ArraysStringsHashTables._01_is_unique.solution import IsUniqueSolution

@pytest.mark.parametrize("klass", [IsUnique, IsUniqueSolution])
def test_is_unique(klass):
    instance = klass()
    try:
        assert instance.is_unique("abcde") is True
        assert instance.is_unique("aAbBcCdDeE") is True
        assert instance.is_unique("abcded") is False
    except NotImplementedError:
        pytest.skip("IsUnique is not implemented yet")
