import pytest
from ch09_Tries._01_title_suggestions.title_suggestions import TitleSuggestions
from ch09_Tries._01_title_suggestions.solution import TitleSuggestionsSolution

@pytest.mark.parametrize("klass", [TitleSuggestions, TitleSuggestionsSolution])
def test_title_suggestions(klass):
    instance = klass()
    try:
        books = ["Whatever", "Book 1", "water", "Book 35"]
        prefixes = ["Wo", "Wa", "Boo", "fr"]
        
        res1 = instance.title_suggestions(books, prefixes, False)
        assert res1 == [False, False, True, False]

        res2 = instance.title_suggestions(books, prefixes, True)
        assert res2 == [False, True, True, False]
    except NotImplementedError:
        pytest.skip("TitleSuggestions is not implemented yet")
