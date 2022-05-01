import functools
from typing import List


# dp solution -> task 213
class Solution:
    def rob(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def backtrack(start: int):
            max_find = 0

            if start >= len(nums):
                return 0

            for i in range(start, len(nums)):
                max_find = max(max_find, nums[i] + backtrack(i + 2))

            return max_find

        return backtrack(0)
