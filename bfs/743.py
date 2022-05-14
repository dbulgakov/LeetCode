import math
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist_dict = defaultdict(list)

        q = []

        for node, next_node, time in times:
            dist_dict[node].append((next_node, time))

            if node == k:
                q.append((next_node, time, 0))

        already_visited = {k: 0}

        for next_node, travel_time, elapsed in q:
            if already_visited.get(next_node, math.inf) > elapsed + travel_time:
                already_visited[next_node] = travel_time + elapsed

                q.extend([(nn, nt, travel_time + elapsed) for nn, nt in dist_dict[next_node]])

        return max(already_visited.values()) if len(already_visited) == n else -1
