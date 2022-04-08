from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0

        for index, value in enumerate(nums):
            if value != 0:
                nums[index], nums[pos] = nums[pos], nums[index]
                pos += 1