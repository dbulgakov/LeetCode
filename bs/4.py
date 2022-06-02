from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small_arr, large_arr = nums1, nums2

        if len(small_arr) > len(large_arr):
            small_arr, large_arr = large_arr, small_arr

        combined_length = len(small_arr) + len(large_arr)
        combined_half = combined_length // 2

        left, right = 0, len(small_arr) - 1

        while True:
            i = left + (right - left) // 2
            j = combined_half - i - 2

            s_left = small_arr[i] if i >= 0 else float('-inf')
            s_right = small_arr[i + 1] if i + 1 < len(small_arr) else float('inf')
            l_left = large_arr[j] if j >= 0 else float('-inf')
            l_right = large_arr[j + 1] if j + 1 < len(large_arr) else float('inf')

            # found median
            if s_left <= l_right and l_left <= s_right:
                if combined_length % 2:
                    return min(s_right, l_right)
                return (max(s_left, l_left) + min(s_right, l_right)) / 2
            elif s_left > l_right:
                right = i - 1
            else:
                left = i + 1
