from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, arr: list[int], sm: int):
            if sm < 0 or len(arr) > k:
                return
            if sm == 0 and len(arr) == k:
                res.append(arr.copy())
                return

            for i in range(start, 10):
                arr.append(i)
                backtrack(i + 1, arr, sm - i)
                arr.pop()

        backtrack(1, [], n)

        return res
