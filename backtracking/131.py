from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(start: int, end: int) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False
                start, end = start + 1, end - 1

            return True

        def backtrack(start: int, part: list[str]) -> None:
            if start >= len(s):
                res.append(list(part))
                return

            for i in range(start, len(s)):
                if is_palindrome(start, i):
                    part.append(s[start:i + 1])
                    backtrack(i + 1, part)
                    part.pop()

        backtrack(0, [])

        return res
