from typing import List, Dict

class TrieNode:
    def __init__(self):
        self.map = {}
        self.word = None

class WordSearchSolution:
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0
        
        root = self._build_trie(words, rows * cols)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.map:
                    self._dfs(board, root, r, c, result)
                    
        return result

    def _dfs(self, board: List[List[str]], current: TrieNode, row: int, col: int, result: List[str]) -> None:
        if current is None:
            return

        if current.word is not None:
            result.append(current.word)
            current.word = None  # Prevent duplicates

        if (row < 0 or row >= len(board) or 
            col < 0 or col >= len(board[0]) or 
            board[row][col] not in current.map):
            return

        current_char = board[row][col]
        board[row][col] = '#'
        
        next_node = current.map[current_char]
        self._dfs(board, next_node, row - 1, col, result)
        self._dfs(board, next_node, row, col + 1, result)
        self._dfs(board, next_node, row + 1, col, result)
        self._dfs(board, next_node, row, col - 1, result)

        board[row][col] = current_char

    def _build_trie(self, words: List[str], max_len: int) -> TrieNode:
        root = TrieNode()
        for word in words:
            if not word or len(word) > max_len:
                continue
            current = root
            for char in word:
                if char not in current.map:
                    current.map[char] = TrieNode()
                current = current.map[char]
            current.word = word
        return root
