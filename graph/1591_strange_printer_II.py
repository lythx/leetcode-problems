from typing import List
from math import inf

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n = max([max(row) for row in targetGrid]) + 1
        G = [[] for _ in range(n)]
        min_x = [inf] * n
        min_y = [inf] * n
        max_x = [-inf] * n
        max_y = [-inf] * n

        for i in range(len(targetGrid)):
            for j in range(len(targetGrid[0])):
                val = targetGrid[i][j]
                min_x[val] = min(min_x[val], i)
                min_y[val] = min(min_y[val], j)
                max_x[val] = max(max_x[val], i)
                max_y[val] = max(max_y[val], j)

        def contains(a, b):
            if min_x[b] == inf:
                return False
            return min_x[a] <= min_x[b] and min_y[a] <= min_y[b] and max_x[a] >= max_x[b] and max_y[a] >= max_y[b]

        def intersecting(a, b):
            if min_x[b] == inf:
                return False
            for i in range(min_x[b], max_x[b] + 1):
                for j in range(min_y[b], max_y[b] + 1):
                    if targetGrid[i][j] == a:
                        return True
            return False

        G = [[] for _ in range(n)]
        for u in range(n - 1):
            for v in range(u + 1, n):
                if contains(u, v):
                    G[u].append(v)
                elif intersecting(v, u):
                    G[u].append(v)
                if contains(v, u):
                    G[v].append(u)
                elif intersecting(u, v):
                    G[v].append(u)

        visited = [0] * n

        def dfs(u):
            for v in G[u]:
                if visited[v] == 2:
                    continue
                if visited[v] == 1:
                    return False
                visited[v] = 1
                if not dfs(v):
                    return False
                visited[v] = 2
            return True

        for u in range(n):
            if visited[u] == 2:
                continue
            visited[u] = 1
            if not dfs(u):
                return False
            visited[u] = 2
        return True