from typing import List


class Solution:
    def isBipartite(self, G: List[List[int]]) -> bool:
        n = len(G)
        color = [0] * n
        vis = [False] * n

        def dfs(u):
            c = color[u]
            for v in G[u]:
                if color[v] == c:
                    return False
                if vis[v]:
                    continue
                vis[v] = True
                color[v] = -color[u]
                if not dfs(v):
                    return False
            return True

        for u in range(n):
            if not vis[u]:
                vis[u] = True
                color[u] = 1
                if not dfs(u):
                    return False
        return True
