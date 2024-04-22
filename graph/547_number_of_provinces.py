from typing import List


class Solution:
    def findCircleNum(self, G: List[List[int]]) -> int:
        n = len(G)
        vis = [0] * n

        def dfs(u):
            for v in range(n):
                if G[u][v] and not vis[v]:
                    vis[v] = True
                    dfs(v)

        ans = 0
        for v in range(n):
            if not vis[v]:
                ans += 1
                dfs(v)
        return ans
