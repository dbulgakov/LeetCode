from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        row_count = len(rooms)
        col_count = len(rooms[0])

        q = []

        for i in range(0, row_count):
            for j in range(0, col_count):
                if rooms[i][j] == 0:
                    q.append((i, j))

        for row, col in q:
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dx
                c = col + dy

                if 0 <= r < row_count and 0 <= c < col_count and rooms[r][c] != -1 and rooms[r][c] == 2147483647:
                    rooms[r][c] = rooms[row][col] + 1
                    q.append((r, c))
