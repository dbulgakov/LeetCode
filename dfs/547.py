from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        n_rows = len(isConnected)
        province_count: int = 0

        def find_province(row) -> int:
            for j, c in enumerate(isConnected[row]):
                if c == 1 and j not in seen:
                    seen.add(j)
                    find_province(j)

            return 1

        for i in range(0, n_rows):
            if i not in seen:
                find_province(i)
                province_count += 1

        return province_count
