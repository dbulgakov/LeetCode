import heapq
from collections import Counter


class Solution:
    # Time: O(n * log n)
    # Space: O(n)

    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        values_dict = Counter(hand)
        heap = list(values_dict.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]

            for i in range(first, first + groupSize):
                if i not in values_dict:
                    return False

                values_dict[i] -= 1

                if values_dict[i] == 0:
                    heapq.heappop(heap)

        return True
