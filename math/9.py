class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        for i in range(0, len(num_str)):
            if num_str[i] != num_str[len(num_str) - i - 1]:
                return False
            return True

        # return str(x) == str(x)[::-1]
