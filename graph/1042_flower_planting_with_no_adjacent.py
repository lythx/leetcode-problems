from typing import List


class Solution:
    def gardenNoAdj(self, n: int, E: List[List[int]]) -> List[int]:
        color = [0] * (n + 1)
        G = [[] for _ in range(n + 1)]
        for u, v in E:
            G[u].append(v)
            G[v].append(u)

        def dfs(u):
            for v in G[u]:
                if color[v] == 0:
                    color[v] = (color[v] % 4) + 1
                    dfs(v)
                elif color[v] == color[u]:
                    color[u] = (color[u] % 4) + 1
                    dfs(u)
                    return

        for u in range(1, n + 1):
            if color[u] == 0:
                color[u] = 1
                dfs(u)
        return color[1:]