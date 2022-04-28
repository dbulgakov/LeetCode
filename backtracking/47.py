from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        nums.sort()

        def backtrack(first: int = 0):
            if first == n:
                res.append(nums.copy())

            processed = set()

            for i in range(first, n):
                if nums[i] not in processed:
                    nums[first], nums[i] = nums[i], nums[first]
                    backtrack(first + 1)
                    nums[first], nums[i] = nums[i], nums[first]
                processed.add(nums[i])

        backtrack()
        return res