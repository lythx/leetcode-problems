from typing import List

class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        m = len(mat)
        n = len(mat[0])
        # histogram
        hg = [0] * (n + 1)
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == "0":
                    hg[j] = 0
                else:
                    hg[j] = hg[j] + 1
            stack = [-1]
            for i in range(n + 1):
                while hg[i] < hg[stack[-1]]:
                    h = hg[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
        return ans
