from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def backtrack(index, total) -> int:
            if index == len(nums):
                return 1 if total == target else 0

            res = 0

            res += backtrack(index + 1, total + nums[index])
            res += backtrack(index + 1, total - nums[index])

            return res

        return backtrack(0, 0)
