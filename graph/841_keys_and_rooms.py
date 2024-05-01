from typing import List


class Solution:
    def canVisitAllRooms(self, G: List[List[int]]) -> bool:
        n = len(G)
        vis = [False] * n

        def dfs(u):
            for v in G[u]:
                if not vis[v]:
                    vis[v] = True
                    dfs(v)

        vis[0] = True
        dfs(0)
        return not (False in vis)
