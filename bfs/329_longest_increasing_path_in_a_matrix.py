from typing import List


class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        p = [[-1] * m for _ in range(n)]

        def dfs(i, j):
            if p[i][j] != -1:
                return p[i][j]
            mx = 0
            if i > 0 and mat[i][j] < mat[i - 1][j]:
                mx = dfs(i - 1, j)
            if i < n - 1 and mat[i][j] < mat[i + 1][j]:
                mx = max(mx, dfs(i + 1, j))
            if j > 0 and mat[i][j] < mat[i][j - 1]:
                mx = max(mx, dfs(i, j - 1))
            if j < m - 1 and mat[i][j] < mat[i][j + 1]:
                mx = max(mx, dfs(i, j + 1))
            p[i][j] = mx + 1
            return mx + 1

        mx = 0
        for i in range(n):
            for j in range(m):
                mx = max(mx, dfs(i, j))
        return mx
