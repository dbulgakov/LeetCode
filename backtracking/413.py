from typing import List


class Solution:
    def __init__(self):
        self.sum = 0

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def slice(start: int) -> int:
            if start < 2:
                return 0

            dp = 0

            if nums[start] - nums[start - 1] == nums[start - 1] - nums[start - 2]:
                dp = 1 + slice(start - 1)
                self.sum += dp
            else:
                slice(start - 1)

            return dp

        slice(len(nums) - 1)
        return self.sum
