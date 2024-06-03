class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        s = "|" + "|".join(s) + "|"
        n = len(s)
        dp = [False] * n
        center = 0
        while center < n:
            radius = 0
            while center - (radius + 1) >= 0 and \
                    center + (radius + 1) < n and \
                    s[center - (radius + 1)] == s[center + (radius + 1)]:
                radius += 1
            dp[center] = radius
            center += 1
        mx = max(dp)
        i = dp.index(mx)
        return s[i - mx:i + mx].replace('|', '')