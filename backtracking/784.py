from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def backtrack(substr: str):
            index = len(substr)

            if index == n:
                res.append(substr)
                return

            if s[index].isalpha():
                backtrack(substr + s[index].swapcase())

            backtrack(substr + s[index])

        backtrack('')
        return res
