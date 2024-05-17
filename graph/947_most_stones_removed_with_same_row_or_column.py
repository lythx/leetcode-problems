from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [u for u in range(n)]
        rank = [0] * n

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xp = find(x)
            yp = find(y)
            if xp == yp:
                return 0
            if rank[xp] > rank[yp]:
                xp, yp = yp, xp
            elif rank[xp] == rank[yp]:
                rank[y] += 1
            parent[xp] = yp
            return 1

        ans = 0
        rows = {}
        cols = {}
        for u, (x, y) in enumerate(stones):
            if x in rows:
                ans += union(rows[x], u)
            rows[x] = u
            if y in cols:
                ans += union(cols[y], u)
            cols[y] = u
        return ans

