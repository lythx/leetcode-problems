from typing import List


class Solution:
    def findTheCity(self, n: int, E: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for u, v, t in E:
            if t <= distanceThreshold:
                dist[u][v] = t
                dist[v][u] = t
        for u in range(n):
            dist[u][u] = 0
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    new_d = dist[u][k] + dist[k][v]
                    if dist[u][v] > new_d and new_d <= distanceThreshold:
                        dist[u][v] = new_d
        mx = -1
        ans = -1
        for u in range(n):
            unreachable = dist[u].count(float('inf'))
            if unreachable >= mx:
                mx = unreachable
                ans = u
        return ans

