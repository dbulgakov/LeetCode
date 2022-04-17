import functools
from typing import List


class Solution:  # TODO dp
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def backtrack(row, col):
            if row == len(triangle) - 1:
                return triangle[row][col]

            left = col
            right = col + 1

            return triangle[row][col] + min(backtrack(row + 1, left), backtrack(row + 1, right))

        return backtrack(0, 0)
