from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        q = deque()

        for dept, arr, price in flights:
            adj[dept].append((arr, price))
            if dept == src:
                q.append((arr, price, 0))

        res = float('inf')
        seen = {}

        while q:
            dept, price, stops = q.popleft()

            if dept == dst and stops <= k:
                res = min(res, price)

            for arr, prc in adj[dept]:
                if seen.get(arr, float('inf')) > price + prc and stops < k:
                    seen[arr] = price + prc

                    q.append((arr, price + prc, stops + 1))

        return res if res != float('inf') else -1
