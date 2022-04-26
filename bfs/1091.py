from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = [(0, 0, 1)]
        n_row = len(grid)
        n_col = len(grid[0])

        if grid[0][0] != 0 or grid[n_row - 1][n_col - 1] != 0:
            return -1

        for row, col, d in q:
            if (row, col) == (n_row - 1, n_col - 1):
                return d

            for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                r = row + dx
                c = col + dy

                if 0 <= r < n_row and 0 <= c < n_col and grid[r][c] == 0:
                    grid[r][c] = 1
                    q.append((r, c, d + 1))

        return -1






