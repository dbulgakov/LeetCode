from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i: int, total_sum: int) -> bool:
            if total_sum == 0:
                return True

            if i == 0 or total_sum < 0:
                return False

            return dfs(i - 1, total_sum - nums[i]) or dfs(i - 1, total_sum)

        nums_sum = sum(nums)

        if nums_sum % 2 != 0:
            return False

        return dfs(len(nums) - 1, nums_sum // 2)
