from functools import cache
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        @cache
        def build_pattern(w: str) -> str:
            letter_dict = {}
            letter_counter = 0
            result = ''

            for letter in w:
                if letter not in letter_dict:
                    letter_dict[letter] = str(letter_counter)
                    letter_counter += 1

                result += letter_dict[letter]

            return result

        base_pattern = build_pattern(pattern)
        res = []

        for word in words:
            word_pattern = build_pattern(word)
            if base_pattern == word_pattern:
                res.append(word)

        return res
