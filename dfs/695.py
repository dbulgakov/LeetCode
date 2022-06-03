from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        max_area = 0

        def dfs(row: int, col: int) -> int:
            if (row, col) in seen or not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] != 1:
                return 0

            seen.add((row, col))

            total_area = 1

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r = row + dr
                c = col + dc

                total_area += dfs(r, c)

            return total_area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, dfs(i, j))

        return max_area
