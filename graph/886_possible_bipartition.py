from typing import List


class Solution:
    def possibleBipartition(self, n: int, E: List[List[int]]) -> bool:
        G = [[] for _ in range(n + 1)]
        for u, v, in E:
            G[u].append(v)
            G[v].append(u)
        # 1 - red, -1 - blue, 0 - not colored
        color = [0] * (n + 1)

        def dfs(u):
            for v in G[u]:
                if color[v] == 0:
                    color[v] = -color[u]
                    if not dfs(v):
                        return False
                elif color[v] == color[u]:
                    return False
            return True

        for u in range(1, n + 1):
            if color[u] == 0:
                color[u] = 1
                if not dfs(u):
                    return False
        return True
            
