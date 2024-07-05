from math import inf
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [inf, triangle[0][0], inf]
        for i in range(1, n):
            new_dp = [inf]
            for j in range(i + 1):
                new_dp.append(min(dp[j], dp[j + 1]) + triangle[i][j])
            new_dp.append(inf)
            dp = new_dp
        return min(dp)
