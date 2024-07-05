class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 + n2 != len(s3):
            return False
        if n1 == 0:
            return s2 == s3
        if n2 == 0:
            return s1 == s3
        dp1 = [False] * (n2 + 1)
        dp2 = [False] * (n2 + 1)
        dp1[0] = True
        dp1[1] = s2[0] == s3[0]
        for j in range(2, n2 + 1):
            if s2[j - 1] != s3[j - 1]:
                break
            dp1[j] = dp1[j - 1]
        for i in range(1, n1 + 1):
            if s1[i - 1] == s3[i - 1]:
                dp2[0] = dp1[0]
            for j in range(1, n2 + 1):
                dp2[j] = (s1[i - 1] == s3[i + j - 1] and dp1[j]) \
                         or (s2[j - 1] == s3[i + j - 1] and dp2[j - 1])
            dp1, dp2 = dp2, dp1
        return dp1[n2]

