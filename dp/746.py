from functools import cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

# recursion
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         @cache
#         def minimum_cost(i):
#             if i <= 1:
#                 return 0
#
#             down_one = cost[i - 1] + minimum_cost(i - 1)
#             down_two = cost[i - 2] + minimum_cost(i - 2)
#             return min(down_one, down_two)
#
#         return minimum_cost(len(cost))
