from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        leftMin = nums[0]

        for n in nums[1:]:
            while stack and stack[-1][0] <= n:
                stack.pop()
            if stack and stack[-1][1] < n:
                return True

            stack.append((n, leftMin))
            leftMin = min(leftMin, n)

        return False
