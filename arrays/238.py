from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res: list[int] = [1] * (len(nums))
        prefix = 1
        postfix = 1

        for i, n in enumerate(nums):
            res[i] = prefix
            prefix *= n

        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]

        return res
