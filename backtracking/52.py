class Solution:
    def __init__(self):
        self.res = 0

    def totalNQueens(self, n: int) -> int:
        cols = set()
        positive_diagonals = set()
        negative_diagonals = set()

        board = [['.'] * n for _ in range(n)]

        def backtrack(row: int) -> None:
            if row == n:
                self.res += 1
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

        return self.res
