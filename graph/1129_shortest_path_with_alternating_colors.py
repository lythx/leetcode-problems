from typing import List
from collections import deque


class Solution:
    def shortestAlternatingPaths(self, n: int, red: List[List[int]], blue: List[List[int]]) -> List[int]:
        Gr = [[] for _ in range(n)]
        for u, v in red:
            Gr[u].append(v)
        Gb = [[] for _ in range(n)]
        for u, v in blue:
            Gb[u].append(v)
        dist_r = [float('inf')] * n
        dist_b = [float('inf')] * n
        q = deque()
        q.append((0, 'r'))
        q.append((0, 'b'))
        dist_r[0] = dist_b[0] = 0
        step = 1
        while len(q) != 0:
            for _ in range(len(q)):
                u, color = q.popleft()
                if color == 'r':
                    for v in Gr[u]:
                        if dist_r[v] == float('inf'):
                            dist_r[v] = step
                            q.append((v, 'b'))
                else:
                    for v in Gb[u]:
                        if dist_b[v] == float('inf'):
                            dist_b[v] = step
                            q.append((v, 'r'))
            step += 1
        return [y if y != float('inf') else -1 for y in [min(x, y) for x, y in zip(dist_r, dist_b)]]
