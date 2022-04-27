from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start: int, arr: List[int]):
            res.append(arr.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()

        backtrack(0, [])

        return res
