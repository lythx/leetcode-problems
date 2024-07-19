from typing import List


class Solution:
    def minCut(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [i for i in range(n + 1)]
        dp[0] = -1
        for center in range(n):
            i = 0
            while center - i >= 0 and center + i < n and s[center - i] == s[center + i]:
                dp[center + i + 1] = min(dp[center + i + 1], dp[center - i] + 1)
                i += 1

            i = 0
            while center - i >= 0 and center + 1 + i < n and s[center - i] == s[center + 1 + i]:
                dp[center + i + 2] = min(dp[center + i + 2], dp[center - i] + 1)
                i += 1

        return dp[-1]
