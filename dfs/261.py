from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connectivity = defaultdict(list)

        for u, v in edges:
            connectivity[u].append(v)
            connectivity[v].append(u)

        seen = set()

        def dfs(node):
            if node in seen:
                return

            seen.add(node)

            for v in connectivity[node]:
                dfs(v)

        dfs(0)

        return len(seen) == n and len(edges) == n - 1
