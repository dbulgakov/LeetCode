from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[len(nums) - 1]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] > nums[len(nums) - 1]:
                left = middle + 1
            elif middle - 1 >= 0 and nums[middle - 1] > nums[middle]:
                return nums[middle]
            else:
                right = middle - 1
