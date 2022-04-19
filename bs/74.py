from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_row():
            top = 0
            bottom = len(matrix) - 1

            while top <= bottom:
                middle = top + (bottom - top) // 2

                if matrix[middle][0] <= target and matrix[middle][len(matrix[middle]) - 1] >= target:
                    return middle
                elif matrix[middle][0] > target:
                    bottom = middle - 1
                else:
                    top = middle + 1

            return -1

        def bs(nums, val):
            start = 0
            end = len(nums) - 1

            while start <= end:
                middle = start + (end - start) // 2

                if nums[middle] == val:
                    return middle
                elif nums[middle] > val:
                    end = middle - 1
                else:
                    start = middle + 1

            return -1

        found_row = find_row()

        if found_row != -1:
            return bs(matrix[found_row], target) != -1
        return False
