from typing import List

class Solution:
    def findRedundantConnection(self, E: List[List[int]]) -> List[int]:
        n = len(E)
        parent = [x for x in range(n + 1)]
        rank = [0] * (n + 1)

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xp = find(x)
            yp = find(y)
            if xp == yp:
                return False
            if rank[xp] > rank[yp]:
                xp, yp = yp, xp
            elif rank[xp] == rank[yp]:
                rank[y] += 1
            parent[xp] = yp
            return yp

        for u, v in E:
            if not union(u, v):
                return [u, v]

