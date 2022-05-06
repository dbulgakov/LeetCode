from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for am in range(1, amount + 1):
            for coin in coins:
                if am - coin >= 0:
                    dp[am] = min(dp[am], 1 + dp[am - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1

# class Solution2:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         q = [(amount, 0)]
#         seen = set()
#
#         for amount_left, coins_used in q:
#             for coin in coins:
#                 diff = amount_left - coin
#                 if diff > 0 and diff not in seen:
#                     seen.add(diff)
#                     q.append((diff, coins_used + 1))
#                 elif diff == 0:
#                     return coins_used + 1
#         return -1


s = Solution()
s.coinChange([2], 3)
