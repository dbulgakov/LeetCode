from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check_dict = {}

        for n in nums:
            check_dict[n] = check_dict.get(n, 0) + 1

        check_dict = {k: v for k, v in sorted(check_dict.items(), key=lambda item: item[1], reverse=True)}

        return list(check_dict.keys())[:k]
