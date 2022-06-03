from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.cache = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for i in range(len(matrix)):
            prev = 0
            for j in range(len(matrix[0])):
                prev += matrix[i][j]
                above = self.cache[i][j + 1]
                self.cache[i + 1][j + 1] = prev + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.cache[row2][col2]
        above = self.cache[row1 - 1][col2]
        left = self.cache[row2][col1 - 1]
        topLeft = self.cache[row1 - 1][col1 - 1]

        return bottomRight - above - left + topLeft


n = NumMatrix([[-1]])
n.sumRegion(*[0, 0, 0, 0])
