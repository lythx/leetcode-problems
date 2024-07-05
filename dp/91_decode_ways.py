class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[index][was_last_decoded_as_double]
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        for i in range(2, n + 1):
            if 10 <= int(s[(i - 2):i]) <= 26:
                dp[i] += dp[i - 2]
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
        return dp[n]

print(Solution().numDecodings("06"))