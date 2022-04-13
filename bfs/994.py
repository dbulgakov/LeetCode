from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])

        q = []
        minutes = 0

        for i in range(0, row_count):
            for j in range(0, col_count):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        for row, col, minute in q:
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dx
                c = col + dy

                if 0 <= r < row_count and 0 <= c < col_count and grid[r][c] == 1:
                    grid[r][c] = 2
                    elapsed = minute + 1
                    minutes = max(minutes, elapsed)
                    q.append((r, c, elapsed))

        for i in range(0, row_count):
            for j in range(0, col_count):
                if grid[i][j] == 1:
                    return -1

        return minutes
