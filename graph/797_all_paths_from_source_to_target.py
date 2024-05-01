from typing import List


class Solution:
    def allPathsSourceTarget(self, G: List[List[int]]) -> List[List[int]]:
        n = len(G)
        vis = [False] * n
        ans = []

        def dfs(u, path):
            if u == n - 1:
                ans.append(path)
            for v in G[u]:
                if not vis[v]:
                    vis[v] = True
                    dfs(v, path + [v])
                    vis[v] = False

        vis[0] = True
        dfs(0, [0])
        return ans
