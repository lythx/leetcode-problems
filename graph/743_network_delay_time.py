from typing import List
from queue import PriorityQueue


class Solution:
    def networkDelayTime(self, E: List[List[int]], n: int, k: int) -> int:
        G = [[] for _ in range(n + 1)]
        for u, v, w in E:
            G[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        pq = PriorityQueue()
        pq.put((0, k))
        while not pq.empty():
            wu, u = pq.get()
            for v, w in G[u]:
                alt = wu + w
                if dist[v] > alt:
                    dist[v] = alt
                    pq.put((alt, v))
        mx = max(dist[1:])
        if mx == float('inf'):
            return -1
        return mx