from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        counter = 0

        for i, v in enumerate(nums):
            if v != val:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
                counter += 1
            else:
                nums[i] = '_'

        return counter


s = Solution()
n = [0, 1, 2, 2, 3, 0, 4, 2]
print(s.removeElement(n, 2))
print(n)