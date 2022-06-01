from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        positive_diagonals = set()
        negative_diagonals = set()

        res = []
        board = [['.'] * n for i in range(n)]

        def backtrack(row: int) -> None:
            if row == n:
                res.append([''.join(row) for row in board])
                return

            for col in range(n):
                if col not in cols and row - col not in negative_diagonals and row + col not in positive_diagonals:
                    cols.add(col)
                    negative_diagonals.add(row - col)
                    positive_diagonals.add(row + col)

                    board[row][col] = 'Q'

                    backtrack(row + 1)

                    board[row][col] = '.'

                    cols.remove(col)
                    negative_diagonals.remove(row - col)
                    positive_diagonals.remove(row + col)

        backtrack(0)

        return res
