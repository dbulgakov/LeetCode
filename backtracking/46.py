from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums.copy()]

        for i in range(0, len(nums)):
            n = nums.pop(0)
            permuted = self.permute(nums)

            for p in permuted:
                p.append(n)

            res.extend(permuted)

            nums.append(n)

        return res
