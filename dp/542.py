from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_count = len(mat)
        col_count = len(mat[0])

        q = []

        for i in range(0, row_count):
            for j in range(0, col_count):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = '#'

        for row, col in q:
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dx
                c = col + dy

                if 0 <= r < row_count and 0 <= c < col_count and mat[r][c] == '#':
                    mat[r][c] = mat[row][col] + 1
                    q.append((r, c))

        return mat

