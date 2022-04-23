from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        s_counter = Counter()
        p_len = len(p)

        res = []

        for i, l in enumerate(s):
            s_counter[l] += 1

            if i >= p_len:
                if s_counter[s[i - p_len]] == 1:
                    del s_counter[s[i - p_len]]
                else:
                    s_counter[s[i - p_len]] -= 1
            if s_counter == p_counter:
                res.append(i - p_len + 1)

        return res
