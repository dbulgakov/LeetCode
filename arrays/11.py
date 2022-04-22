from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calc_area(left: int, right: int) -> int:
            l_height = height[left]
            r_height = height[right]

            return (right - left) * min(l_height, r_height)

        l, r = 0, len(height) - 1
        total_area = calc_area(l, r)

        while l < r:
            total_area = max(calc_area(l, r), total_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return total_area
