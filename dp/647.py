class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def expand(l: int, r: int) -> int:
            counter = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1

            return counter

        for i in range(len(s)):
            res += expand(i, i)
            res += expand(i, i + 1)

        return res
