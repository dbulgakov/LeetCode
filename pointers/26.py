from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0

        for i in range(0, len(nums)):
            if nums[i] != nums[pos]:
                pos += 1
                nums[pos] = nums[i]
        return pos + 1
