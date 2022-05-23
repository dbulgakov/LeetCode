from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []

        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                val, stack_index = s.pop()
                res[stack_index] = i - stack_index

            s.append((t, i))

        return res
