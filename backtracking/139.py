from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @cache
        def word_break(s: str, start: int) -> bool:
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set and word_break(s, end):
                    return True

            return False

        return word_break(s, 0)
