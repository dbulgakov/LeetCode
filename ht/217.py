from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        for i, e in enumerate(nums):
            if e in ht:
                return True
            else:
                ht[e] = e
        return False
