from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        n_rows = len(grid)
        n_col = len(grid[0])
        counter: int = 0

        def check_area(row: int, col: int) -> int:
            if not ((row, col) not in seen and 0 <= row < n_rows and 0 <= col < n_col and grid[row][col] == '1'):
                return 0

            seen.add((row, col))

            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                check_area(row + dx, col + dy)

            return 1

        for i in range(0, n_rows):
            for j in range(0, n_col):
                counter += check_area(i, j)

        return counter
