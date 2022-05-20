import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-math.sqrt(x ** 2 + y ** 2), [x, y]) for x, y in points[:k]]

        heapq.heapify(heap)

        for x, y in points[k:]:
            distance = math.sqrt(x ** 2 + y ** 2)

            if -distance > heap[0][0]:
                heapq.heappushpop(heap, (-distance, [x, y]))

        return [x[1] for x in heap]
