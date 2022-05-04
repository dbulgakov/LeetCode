from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def backtrack(index: int) -> int:
            if index == len(s):
                return 1

            if index > len(s) or s[index] == '0':
                return 0

            answer = backtrack(index + 1)
            if int(s[index: index + 2]) <= 26:
                answer += backtrack(index + 2)

            return answer

        return backtrack(0)
