from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for index, num in enumerate(nums):
            delta = target - num
            if delta in hash_table:
                return [index, hash_table[delta]]
            hash_table[num] = index
