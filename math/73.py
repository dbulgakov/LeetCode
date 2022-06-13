from collections import deque
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        q = deque()
        row_set = set()
        col_set = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 and i not in row_set and j not in col_set:
                    q.append((i, j))

        while q:
            row, col = q.popleft()

            for i in range(len(matrix[0])):
                matrix[row][i] = 0

            for j in range(len(matrix)):
                matrix[j][col] = 0