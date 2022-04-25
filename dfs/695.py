from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen_dict = set()
        row_count = len(grid)
        col_count = len(grid[0])

        def check_area(row, col):
            if not (0 <= row < row_count and 0 <= col < col_count
                    and (row, col) not in seen_dict and grid[row][col] == 1):
                return 0
            seen_dict.add((row, col))

            return 1 + check_area(row + 1, col) \
                   + check_area(row - 1, col) \
                   + check_area(row, col + 1) \
                   + check_area(row, col - 1)

        return max(check_area(r, c)
                   for r in range(row_count)
                   for c in range(col_count))
