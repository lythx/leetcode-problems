from typing import List
from queue import PriorityQueue


class Solution:
    def shortestPathLength(self, G: List[List[int]]) -> int:
        n = len(G)
        k = pow(2, n)
        dist = [[float('inf')] * k for _ in range(n)]
        pq = PriorityQueue()
        for u in range(n):
            mask = pow(2, u)
            dist[u][mask] = 0
            pq.put((u, mask))
        while not pq.empty():
            u, mask = pq.get()
            for v in G[u]:
                new_mask = mask | (1 << v)
                if dist[v][new_mask] > dist[u][mask] + 1:
                    dist[v][new_mask] = dist[u][mask] + 1
                    pq.put((v, new_mask))
        ans = float('inf')
        for u in range(n):
            ans = min(ans, dist[u][k - 1])
        return ans
                    

        
