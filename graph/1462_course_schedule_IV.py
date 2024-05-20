from typing import List


class Solution:
    def checkIfPrerequisite(self, n: int, E: List[List[int]], queries: List[List[int]]) -> List[bool]:
        path = [[False] * n for _ in range(n)]
        for u in range(n):
            path[u][u] = True
        for u, v in E:
            path[u][v] = True
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    if path[u][k] and path[k][v]:
                        path[u][v] = True
        return [path[u][v] for u, v in queries]
