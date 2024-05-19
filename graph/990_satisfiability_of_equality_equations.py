from typing import List
from string import ascii_lowercase
from queue import PriorityQueue

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {x: x for x in ascii_lowercase}
        rank = {x: 0 for x in ascii_lowercase}

        def find(x):
            if parent[x] == x:
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

        for x, form, _, y in equations:
            if form == "=":
                union(x, y)
        for x, form, _, y in equations:
            if form == "!" and (find(x) == find(y)):
                return False
        return True
