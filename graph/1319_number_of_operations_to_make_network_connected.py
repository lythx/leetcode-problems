from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        G = [[] for _ in range(n)]
        for u, v in connections:
            G[u].append(v)
            G[v].append(u)
        visited = [False] * n

        def dfs(u):
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    dfs(v)

        count = 0
        for u in range(n):
            if not visited[u]:
                count += 1
                visited[u] = True
                dfs(u)

        return count - 1
