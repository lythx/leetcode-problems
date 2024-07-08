from typing import List
from math import inf

class Solution:
    def maxProfit(self, k: int, P: List[int]) -> int:
        n = len(P)
        memo = [[[-inf, -inf] for _ in range(k + 1)] for _ in range(n)]
        for i in range(k + 1):
            memo[0][i][0] = 0
            memo[0][i][1] = -P[0]
        print(memo)

        # i=max index, t=transaction count, b=bought stock
        def f(i, t, b):
            if t == -1 or i == -1:
                return -inf
            if memo[i][t][b] != -inf:
                return memo[i][t][b]
            if b == 1:
                memo[i][t][b] = max(f(i - 1, t, 1), f(i - 1, t, 0) - P[i])
            else:
                memo[i][t][b] = max(f(i - 1, t, 0), f(i - 1, t - 1, 1) + P[i])
            return memo[i][t][b]

        return max(f(n - 1, k, 0), f(n - 1, k, 1))

Solution().maxProfit(2, [2,4,1])

