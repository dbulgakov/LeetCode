from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates_len = len(candidates)

        candidates.sort()

        def backtrack(target_sum: int, arr: List[int], start: int):
            if target_sum < 0:
                return

            if target_sum == 0:
                res.append(arr.copy())
                return

            for i in range(start, candidates_len):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                backtrack(target_sum - candidates[i], arr, i + 1)
                arr.pop()

        backtrack(target, [], 0)
        return res


s = Solution()
print(s.combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
