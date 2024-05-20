from typing import List
from queue import PriorityQueue

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        nm = n * m
        G = [[] for _ in range(nm)]

        def f(i, j):
            return i * m + j

        for i in range(n):
            for j in range(m):
                if j < m - 1:
                    G[f(i, j)].append((f(i, j + 1), grid[i][j] == 1))
                if j > 0:
                    G[f(i, j)].append((f(i, j - 1), grid[i][j] == 2))
                if i < n - 1:
                    G[f(i, j)].append((f(i + 1, j), grid[i][j] == 3))
                if i > 0:
                    G[f(i, j)].append((f(i - 1, j), grid[i][j] == 4))

        pq = PriorityQueue()
        pq.put((0, 0))
        dist = [float('inf')] * nm
        dist[0] = 0
        while not pq.empty():
            d, u = pq.get()
            if u == nm - 1:
                break
            for v, free in G[u]:
                new_d = d + (1 - int(free))
                if new_d < dist[v]:
                    dist[v] = new_d
                    pq.put((new_d, v))
        return dist[nm - 1]
