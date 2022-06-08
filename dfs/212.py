from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        visited = set()

        n_rows = len(board)
        n_cols = len(board[0])

        def dfs(row: int, col: int, parent_node: dict, word: str) -> None:
            node = parent_node[word[-1]]

            if 'end' in node:
                res.add(word)

            if not any(node) or len(node.keys()) == 1 and 'end' in node:
                del parent_node[word[-1]]
                return

            visited.add((row, col))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r = row + dr
                c = col + dc

                if (0 <= r < n_rows and 0 <= c < n_cols) \
                        and (r, c) not in visited \
                        and board[r][c] in node:
                    dfs(r, c, node, word + board[r][c])

            visited.remove((row, col))

        def grab_node() -> dict[dict]:
            node = {}
            node_start = node

            for word in words:
                node = node_start
                for letter in word:
                    if letter not in node:
                        node[letter] = {}
                    node = node[letter]
                node['end'] = True

            return node_start

        letter_node = grab_node()

        if not board or not board[0]:
            return res

        for i in range(n_rows):
            for j in range(n_cols):
                letter = board[i][j]
                if letter in letter_node and len(res) != len(words):
                    dfs(i, j, letter_node, letter)

        return list(res)
