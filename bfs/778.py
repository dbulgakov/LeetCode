import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        q = [(grid[0][0], 0, 0)]

        seen = {0, 0}

        while q:
            duration, row, col = heapq.heappop(q)

            if row == len(grid) - 1 and col == len(grid) - 1:
                return duration

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r = row + dr
                c = col + dc

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen:
                    new_duration = max(duration, grid[r][c])
                    seen.add((r, c))
                    heapq.heappush(q, (new_duration, r, c))

        return -1
