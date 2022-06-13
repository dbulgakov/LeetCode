class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = ''

        def expand(l: int, r: int) -> str:
            counter = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1

            if counter > longest:
                return s[l:r+1]
            return res

        for i in range(len(s)):
            res = expand(i, i)
            res = expand(i, i + 1)

        return res
