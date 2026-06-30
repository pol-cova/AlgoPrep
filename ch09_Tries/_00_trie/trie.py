from ch09_Tries._00_trie.trie_node import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        lowercase_word = word.lower()
        for char in lowercase_word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, prefix: str) -> bool:
        current_node = self.root
        prefix_lowercase = prefix.lower()
        for char in prefix_lowercase:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True
