class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        longest = 0

        for i in range(0, len(s)):
            left = right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    res = s[left: right + 1]
                    longest = right - left + 1
                left -= 1
                right += 1

            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    res = s[left: right + 1]
                    longest = right - left + 1
                left -= 1
                right += 1

        return res


