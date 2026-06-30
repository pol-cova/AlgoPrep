from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self, ignore_case: bool):
        self.root = TrieNode()
        self.ignore_case = ignore_case

    def insert(self, word: str) -> None:
        current = self.root
        to_insert = word.lower() if self.ignore_case else word
        for char in to_insert:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

    def search(self, prefix: str) -> bool:
        current = self.root
        to_search = prefix.lower() if self.ignore_case else prefix
        for char in to_search:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

class TitleSuggestionsSolution:
    def title_suggestions(self, books: List[str], prefixes: List[str], ignore_case: bool) -> List[bool]:
        dictionary = Trie(ignore_case)
        for book in books:
            dictionary.insert(book)
            
        return [dictionary.search(p) for p in prefixes]
