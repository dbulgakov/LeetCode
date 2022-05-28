from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        arr_sum = n * (n - 1) // 2
        num_sum = sum(nums)

        return arr_sum - num_sum
