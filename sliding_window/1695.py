from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        duplication_dict = {}
        prefix_sum = [0] * (len(nums) + 1)

        start = 0
        res = 0

        for i, n in enumerate(nums):
            prefix_sum[i + 1] = prefix_sum[i] + n
            if n in duplication_dict:
                start = max(start, duplication_dict[n] + 1)

            duplication_dict[n] = i
            res = max(res, prefix_sum[i + 1] - prefix_sum[start])

        return res
