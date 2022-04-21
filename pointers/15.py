from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, value in enumerate(nums):
            if value > 0:
                break
            if index == 0 or nums[index - 1] != nums[index]:
                self.twoSum(nums, index, res)

        return res

    def twoSum(self, nums: List[int], index: int, res: List[List[int]]):
        left = index + 1
        right = len(nums) - 1

        while left < right:
            target_sum = nums[index] + nums[left] + nums[right]

            if target_sum < 0:
                left += 1
            elif target_sum > 0:
                right -= 1
            else:
                res.append([nums[index], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1