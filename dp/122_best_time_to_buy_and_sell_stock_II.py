from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prev_not_bought = 0
        prev_bought = -prices[0]
        for i in range(1, n):
            not_bought = max(prev_not_bought, prev_bought + prices[i])
            bought = max(prev_bought, prev_not_bought - prices[i])
            prev_not_bought = not_bought
            prev_bought = bought
        return prev_not_bought
