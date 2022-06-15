from typing import List


class Solution:
    # Time: O(n * l), l - max word len
    # Space: O(n)

    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=lambda word: len(word))
        d = {word: 1 for word in words}
        res = 1

        for word in words:
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in d:
                    d[word] = max(1 + d[prev], d[word])
                    res = max(res, d[word])

        return res
