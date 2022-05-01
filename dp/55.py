from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable_index = 0
        for curr in range(len(nums)):
            if curr + nums[curr] >= reachable_index:
                reachable_index = curr + nums[curr]
            if curr == reachable_index:
                break

        return reachable_index >= len(nums) - 1
