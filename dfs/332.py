from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        connectivity = defaultdict(list)

        tickets.sort()

        res = ['JFK']

        def dfs(source: str) -> bool:
            if len(res) == len(tickets) + 1:  # due to + JFK
                return True
            if source not in connectivity:
                return False

            connectivity_copy = list(connectivity[source])

            for index, city in enumerate(connectivity_copy):
                res.append(city)
                connectivity[source].pop(index)

                if dfs(city):
                    return True

                connectivity[source].insert(index, city)
                res.pop()

            return False

        for source, dest in tickets:
            connectivity[source].append(dest)

        dfs('JFK')

        return res
