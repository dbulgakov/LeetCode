from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(most_left: bool = True) -> int:
            left = 0
            right = len(nums) - 1

            while left <= right:
                middle = left + (right - left) // 2

                if nums[middle] == target:
                    if most_left:
                        if middle == left or nums[middle - 1] != target:
                            return middle
                        else:
                            right = middle - 1
                    else:
                        if middle == right or nums[middle + 1] != target:
                            return middle
                        else:
                            left = middle + 1
                elif nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1

            return -1

        first_index = binary_search(True)
        last_index = binary_search(False)

        return [first_index, last_index]


s = Solution()
print(s.searchRange([1], 1))
