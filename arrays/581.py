from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = list(nums)
        sorted_nums.sort()

        diff_start = len(nums)
        diff_end = 0

        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                diff_start = min(diff_start, i)
                diff_end = max(diff_end, i)

        return (diff_end - diff_start) + 1 if diff_end else 0


class SolutionTwo:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = len(nums), 0

        stack = []
        for i in reversed(range(len(nums))):  # finding end index of unsorted subarray
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end, stack.pop())
            stack.append(i)

        stack = []
        for i in range(len(nums)):  # finding start index of unsorted subarray
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start, stack.pop())
            stack.append(i)

        res = end - start + 1
        return res if res > 0 else 0
