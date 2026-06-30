from typing import List, Set

class WordBreakSolution:
    def word_break(self, s: str, word_dict: List[str]) -> bool:
        memo = [False] * (len(s) + 1)
        return self._word_break_helper(s, set(word_dict), memo)

    def _word_break_helper(self, s: str, word_dict_set: Set[str], memo: List[bool]) -> bool:
        if memo[len(s)]:
            return False
        for i in range(1, len(s) + 1):
            first_word = s[0:i]
            if first_word in word_dict_set:
                second_word = s[i:]
                if (len(second_word) == 0 or 
                    second_word in word_dict_set or 
                    self._word_break_helper(second_word, word_dict_set, memo)):
                    return True
        memo[len(s)] = True
        return False
