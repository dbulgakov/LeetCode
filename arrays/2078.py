from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0

        for i in range(len(colors)):
            for j in range(i + 1, len(colors)):
                if colors[j] != colors[i]:
                    max_dist = max(max_dist, abs(j - i))

        return max_dist
