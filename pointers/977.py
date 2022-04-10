from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        last_negative_index = None
        last_negative_value = None

        result = []

        for index, value in enumerate(nums):
            if value < 0:
                last_negative_index = index
                last_negative_value = value
            elif value == 0:
                result.append(0)
            else:
                if last_negative_index is not None and value >= abs(last_negative_value):
                    reverse_index = last_negative_index

                    while reverse_index >= 0 and abs(nums[reverse_index]) <= value:
                        result.append(nums[reverse_index] ** 2)
                        reverse_index = reverse_index - 1

                    last_negative_index = reverse_index if reverse_index >= 0 else None
                    last_negative_value = nums[reverse_index] if reverse_index is not None else None

                result.append(value ** 2)

        while last_negative_index is not None and last_negative_index >= 0:
            result.append(nums[last_negative_index] ** 2)
            last_negative_index -= 1

        return result
