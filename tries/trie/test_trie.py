import pytest
from tries.trie.trie import Trie

def test_trie():
    t = Trie()
    t.insert("Hola")
    t.insert("Mundo")
    t.insert("hola")
    
    assert t.search("ho") is True
    assert t.search("hola") is True
    assert t.search("mun") is True
    assert t.search("xyz") is False
