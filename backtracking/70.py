import functools


class Solution:
    def climbStairs(self, n: int) -> int:
        @functools.lru_cache(None)
        def backtracking(start):
            if start > n:
                return 0

            if start == n:
                return 1

            return backtracking(start + 1) + backtracking(start + 2)

        return backtracking(0) if n > 0 else 0
