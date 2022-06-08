from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connectivity = defaultdict(list)
        seen = set()
        res = 0

        def dfs(source: int) -> None:
            if source in seen:
                return

            seen.add(source)

            for nei in connectivity[source]:
                dfs(nei)

        for u, v in edges:
            connectivity[u].append(v)
            connectivity[v].append(u)

        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1

        return res
