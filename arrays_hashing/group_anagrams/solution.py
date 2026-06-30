from typing import List

class GroupAnagramsSolution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        anagram_map = {}
        for s in strs:
            hash_val = self._get_anagram_hash(s)
            if hash_val not in anagram_map:
                anagram_map[hash_val] = []
            anagram_map[hash_val].append(s)

        return list(anagram_map.values())

    def _get_anagram_hash(self, s: str) -> str:
        letter_count = [0] * 26
        for char in s:
            letter_count[ord(char) - ord('a')] += 1
        return str(letter_count)
