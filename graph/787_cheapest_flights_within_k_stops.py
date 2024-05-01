from typing import List
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, E: List[List[int]], src: int, dst: int, k: int) -> int:
        max_cost = 100000
        G = [[] for _ in range(n)]
        for u, v, p in E:
            G[u].append((v, p))
        cost = [max_cost] * n
        q = deque()
        q.append((src, 0))
        cost[src] = 0
        i = 0
        while len(q) != 0 and i <= k:
            for _ in range(len(q)):
                u, c = q.popleft()
                for v, p in G[u]:
                    if cost[v] > c + p:
                        cost[v] = c + p
                        q.append((v, c + p))
            i += 1
        if cost[dst] == max_cost:
            return -1
        return cost[dst]
