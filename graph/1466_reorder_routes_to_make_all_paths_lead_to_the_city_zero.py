from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        G0 = [[] for _ in range(n)]
        G1 = [[] for _ in range(n)]
        for u, v in connections:
            G0[v].append(u)
            G1[u].append(v)
        visited = [False] * n

        def dfs(u):
            s = 0
            for v in G0[u]:
                if not visited[v]:
                    visited[v] = True
                    s += dfs(v)
            for v in G1[u]:
                if not visited[v]:
                    visited[v] = True
                    s += dfs(v) + 1
            return s

        visited[0] = True
        return dfs(0)