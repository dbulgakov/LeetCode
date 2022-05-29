from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        @cache
        def get_word_set(word: str) -> set[str]:
            return set(word)

        max_perm = 0
        for i in range(len(words) - 1 // 2):
            first_word = get_word_set(words[i])

            for j in range(i, len(words)):
                second_word = get_word_set(words[j])

                if not any(set.intersection(first_word, second_word)):
                    max_perm = max(max_perm, len(words[i]) * len(words[j]))

        return max_perm


class Solution2:
    def maxProduct(self, words: List[str]) -> int:
        hashmap = defaultdict(int)
        bit_number = lambda ch: ord(ch) - ord('a')

        for word in words:
            bitmask = 0
            for ch in word:
                # add bit number bit_number in bitmask
                bitmask |= 1 << bit_number(ch)
            # there could be different words with the same bitmask
            # ex. ab and aabb
            hashmap[bitmask] = max(hashmap[bitmask], len(word))

        max_prod = 0
        for x in hashmap:
            for y in hashmap:
                if x & y == 0:
                    max_prod = max(max_prod, hashmap[x] * hashmap[y])
        return max_prod
