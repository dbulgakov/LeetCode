from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        counter = 0

        def search_island(r: int, c: int) -> int:
            if (r, c) in seen or not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != '1':
                return 0

            seen.add((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                search_island(r + dr, c + dc)

            return 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                counter += search_island(i, j)

        return counter