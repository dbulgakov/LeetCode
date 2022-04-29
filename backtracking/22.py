from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(braces: str, open_brace: int, close_brace: int):
            if open_brace == 0 and close_brace == 0:
                res.append(braces)
                return

            if open_brace > 0:
                backtrack(braces + '(', open_brace - 1, close_brace)

            if close_brace > open_brace:
                backtrack(braces + ')', open_brace, close_brace - 1)

        backtrack('', n, n)

        return res
