from math import inf

class Solution:
    def maxProfit(self, P: List[int]) -> int:
        n = len(P)
        # best single transaction profit up to index
        dp = [-1] * n
        mn = P[0]
        for i in range(1, n):
            if P[i] < mn:
                mn = P[i]
            dp[i] = max(P[i] - mn, dp[i - 1])
        mx = P[-1]
        max_profit = max(dp[-1], 0)
        for i in reversed(range(2, n)):
            if P[i] > mx:
                mx = P[i]
            profit = mx - P[i] + dp[i - 1]
            if profit > max_profit:
                max_profit = profit
        return max_profit
