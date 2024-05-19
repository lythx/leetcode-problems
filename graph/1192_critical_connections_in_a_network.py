from typing import List


class Solution:
    def criticalConnections(self, n: int, E: List[List[int]]) -> List[List[int]]:
        G = [[] for _ in range(n)]
        for u, v in E:
            G[u].append(v)
            G[v].append(u)
        dist = [-1] * n
        low = [-1] * n
        ans = []

        def dfs(u, parent, d):
            dist[u] = d
            low[u] = d
            for v in G[u]:
                if dist[v] == -1:
                    dfs(v, u, d + 1)
                    low[u] = min(low[u], low[v])
                elif v != parent:
                    low[u] = min(low[u], dist[v])
            if low[u] == d and parent is not None:
                ans.append((parent, u))

        dfs(0, None, 0)
        return ans

