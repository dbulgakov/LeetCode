from functools import cache


class Solution:
    # Time: O(m * n), m - len(s1), n - len(s2)
    # Space: O(m * n)

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dfs(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2):
                return i + j == len(s3)

            if i + j >= len(s3):
                return False

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True

            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True

            return False

        return dfs(0, 0)
