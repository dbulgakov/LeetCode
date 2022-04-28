from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates_len = len(candidates)

        def backtrack(target_sum: int, arr: List[int], start: int):
            if target_sum < 0:
                return

            if target_sum == 0:
                res.append(arr.copy())
                return

            for i in range(start, candidates_len):
                arr.append(candidates[i])
                backtrack(target_sum - candidates[i], arr, i)
                arr.pop()

        backtrack(target, [], 0)
        return res
