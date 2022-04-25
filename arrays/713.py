from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or k == 0:
            return 0

        counter = 0

        for i in range(0, len(nums)):
            if nums[i] < k:
                counter += 1

                product = nums[i]

                for j in range(i + 1, len(nums)):
                    product = product * nums[j]
                    if product < k:
                        counter += 1
                    else:
                        break

        return counter
