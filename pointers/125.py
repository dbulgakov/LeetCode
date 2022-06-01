class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if str.isalnum(s[left]) and str.isalnum(s[right]):
                if str.lower(s[left]) != str.lower(s[right]):
                    return False
                left, right = left + 1, right - 1
            else:
                left = left + 1 if not str.isalnum(s[left]) else left
                right = right - 1 if not str.isalnum(s[right]) else right

        return True
