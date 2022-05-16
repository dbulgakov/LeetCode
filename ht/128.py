from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_length = 0

        for n in nums:
            local_max = 0
            if n - 1 not in nums_set:
                while n in nums_set:
                    local_max += 1
                    n += 1

                max_length = max(max_length, local_max)

        return max_length
