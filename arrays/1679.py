from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ht = {}
        counter = 0

        for n in nums:
            ht[n] = ht.get(n, 0) + 1

        for n in nums:
            diff = k - n
            if diff in ht and ht[diff] > 0:
                ht[diff] -= 1
                counter += 1

        return counter // 2
