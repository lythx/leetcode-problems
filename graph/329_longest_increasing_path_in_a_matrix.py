from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        adj = [[] for _ in range(n**2)]
        for i in range(n):
            for j in range(n):
                if i > 0 and matrix[i][j] < matrix[i - 1][j]:
                    adj[i * n + j].append(matrix[i - 1][j])
                if i < n - 1 and matrix[i][j] < matrix[i + 1][j]:
                    adj[i * n + j].append(matrix[i + 1][j])
                if j > 0 and matrix[i][j] < matrix[i][j - 1]:
                    adj[i * n + j].append(matrix[i][j - 1])
                if j < n - 1 and matrix[i][j] < matrix[i][j + 1]:
                    adj[i * n + j].append(matrix[i][j + 1])
        paths = [0] * (n**2)

        def dfs(v):
            if paths[v] != 0:
                return paths[v]
            mx = 0
            for u in adj[v]:
                mx = max(mx, dfs(u))
            paths[v] = mx + 1
            return mx + 1

        max_path = 0
        for i in range(n**2):
            if paths[i] == 0:
                max_path = max(max_path, dfs(i))
            else:
                max_path = max(max_path, paths[i])
        return max_path

