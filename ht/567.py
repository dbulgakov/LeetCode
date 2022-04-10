import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = collections.Counter(s1)
        s1_len = len(s1)

        for i in range(0, len(s2) - s1_len + 1):
            if collections.Counter(s2[i:i+s1_len]) == s1_map:
                return True
        return False

