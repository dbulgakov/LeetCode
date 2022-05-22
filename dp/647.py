from functools import cache


class Solution:
    def countSubstrings(self, s: str) -> int:
        @cache
        def is_palindrome(i, j):
            if i >= j:
                return True
            return s[i] == s[j] and is_palindrome(i + 1, j - 1)

        return sum(is_palindrome(i, j) for i in range(len(s)) for j in range(i, len(s)))
