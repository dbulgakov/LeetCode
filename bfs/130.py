from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = []
        n_row = len(board)
        n_col = len(board[0])

        for i in range(0, n_col):
            if board[0][i] == 'O':
                board[0][i] = 'S'
                q.append((0, i))

            if board[n_row - 1][i] == 'O':
                board[n_row - 1][i] = 'S'
                q.append((n_row - 1, i))

        for i in range(0, n_row):
            if board[i][0] == 'O':
                board[i][0] = 'S'
                q.append((i, 0))
            if board[i][n_col - 1] == 'O':
                board[i][n_col - 1] = 'S'
                q.append((i, n_col - 1))

        for row, col in q:
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dx
                c = col + dy

                if 0 <= r < n_row and 0 <= c < n_col and board[r][c] == 'O':
                    board[r][c] = 'S'
                    q.append((r, c))

        for i in range(0, n_row):
            for j in range(0, n_col):
                board[i][j] = 'X' if board[i][j] != 'S' else 'O'
