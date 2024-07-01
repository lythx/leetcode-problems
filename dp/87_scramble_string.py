class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # dp[k][i][j] - k=len, i=s1 index, j=s2 index
        dp = [[[False] * n for _ in range(n)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[1][i][j] = True
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    for d in range(1, k):
                        left = dp[d][i][j]
                        right = dp[k - d][i + d][j + d]
                        swapleft = dp[d][i][j + k - d]
                        swapright = dp[k - d][i + d][j]
                        if (left and right) or (swapleft and swapright):
                            dp[k][i][j] = True
                            break

        return dp[n][0][0]
