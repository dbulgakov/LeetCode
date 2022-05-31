class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(x: int, y: int, w: str, visited: set[tuple[int, int]]):
            if w == '':
                return True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r = x + dx
                c = y + dy
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and (r, c) not in visited:
                    if board[r][c] == w[0] and dfs(r, c, w[1:], visited | {(r, c)}):
                        return True

            return False

        if not board or not board[0]:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, word[1:], set() | {(i, j)}):
                    return True
        return False
