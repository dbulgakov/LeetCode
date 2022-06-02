from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            combined_sum = numbers[left] + numbers[right]

            if combined_sum == target:
                return [left + 1, right + 1]
            elif combined_sum > target:
                right -= 1
            else:
                left += 1
