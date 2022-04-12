from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        cumulative = 0
        while i >= 0:
            res = digits[i] + cumulative

            if i == len(digits) - 1:
                res += 1

            if res > 9:
                cumulative = res // 10
                res = res % 10
            else:
                cumulative = 0

            digits[i] = res

            i -= 1

        if cumulative > 0:
            return [cumulative] + digits

        return digits