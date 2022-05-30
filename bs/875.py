import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_duration(speed: int) -> int:
            res = 0
            for p in piles:
                res += int(math.ceil(p / speed))
            return res

        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = left + (right - left) // 2
            duration = calculate_duration(mid)

            if duration <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res
