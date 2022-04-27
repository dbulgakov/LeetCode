from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start: int, arr: List[int]):
            res.append(arr.copy())

            for i in range(start, len(nums)):
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()

        backtrack(0, [])

        return res
