from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        max_profit = 0
        for p in prices[1:]:
            max_profit = max(max_profit, p - cost)
            cost = min(cost, p)
        return max_profit
