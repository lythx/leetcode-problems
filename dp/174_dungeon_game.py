from typing import List
from math import inf

class Solution:
    def calculateMinimumHP(self, D: List[List[int]]) -> int:
        m = len(D)
        n = len(D[0])
        dp = [[inf] * n for _ in range(m)]
        dp[m - 1][n - 1] = max(1 - D[m - 1][n - 1], 1)
        for i in reversed(range(m - 1)):
            dp[i][-1] = max(dp[i + 1][-1] - D[i][-1], 1)
        for i in reversed(range(n - 1)):
            dp[-1][i] = max(dp[-1][i + 1] - D[-1][i], 1)
        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - D[i][j], 1)
        return dp[0][0]

