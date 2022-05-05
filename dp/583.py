import functools


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        longest_subsec = self.longestCommonSubsequence(word1, word2)

        if longest_subsec > 0:
            return len(word1) - longest_subsec + len(word2) - longest_subsec
        return len(word1) + len(word2)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @functools.cache
        def check_subsequence(first_pointer: int, second_pointer: int) -> int:
            if first_pointer == len(text1) or second_pointer == len(text2):
                return 0

            if text1[first_pointer] == text2[second_pointer]:
                return 1 + check_subsequence(first_pointer + 1, second_pointer + 1)
            else:
                return max(check_subsequence(first_pointer + 1, second_pointer),
                           check_subsequence(first_pointer, second_pointer + 1))

        return check_subsequence(0, 0)