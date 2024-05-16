from queue import PriorityQueue
from typing import List


class Solution:
    def reachableNodes(self, E: List[List[int]], maxMoves: int, n: int) -> int:
        G: List[List[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, c in E:
            G[u].append((v, c + 1))
            G[v].append((u, c + 1))
        dist = [float('inf')] * n
        dist[0] = 0
        pq = PriorityQueue()
        pq.put((0, 0))
        while not pq.empty():
            moves, u = pq.get()
            for v, c in G[u]:
                if moves + c < dist[v] and moves + c <= maxMoves:
                    dist[v] = moves + c
                    pq.put((dist[v], v))
        ans = 0
        for u, v, c in E:
            moves_u = max(maxMoves - dist[u], 0)
            moves_v = max(maxMoves - dist[v], 0)
            ans += min(moves_u + moves_v, c)
        for d in dist:
            if d != float('inf'):
                ans += 1
        return ans

