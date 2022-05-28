from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        arr_sum = n * (n - 1) // 2
        num_sum = 0

        for number in nums:
            num_sum += number

        return abs(arr_sum - num_sum)