from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        def in_radius(r, x1, y1, x2, y2):
            dx = x2 - x1
            dy = y2 - y1
            return dx*dx + dy*dy <= r*r

        G = [[] for _ in range(n)]
        for i, (x1, y1, r) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if i != j and in_radius(r, x1, y1, x2, y2):
                    G[i].append(j)

        visited = [False] * n
        def dfs(u):
            count = 1
            for v in G[u]:
                if visited[v]:
                    continue
                visited[v] = True
                count += dfs(v)
            return count

        mx = 0
        for u in range(n):
            visited = [False] * n
            visited[u] = True
            mx = max(mx, dfs(u))
        return mx