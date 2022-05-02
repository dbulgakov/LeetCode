from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pos = 0

        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        return nums
