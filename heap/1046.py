import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_stone = heapq.heappop(stones)
            second_stone = heapq.heappop(stones)

            if first_stone != second_stone:
                heapq.heappush(stones, first_stone - second_stone)

        return -stones[0] if any(stones) else 0
