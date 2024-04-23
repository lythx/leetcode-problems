from typing import List


class Solution:
    def findRedundantDirectedConnection(self, E: List[List[int]]) -> List[int]:
        n = len(E)
        parent = [-1] * (n + 1)
        double_edge_ind = -1
        second_double_edge = None
        for i in range(n):
            u, v = E[i]
            if parent[v] != -1:
                double_edge_ind = i
                second_double_edge = [parent[v], v]
                break
            else:
                parent[v] = u
        if double_edge_ind != -1:
            G = [[] for _ in range(n + 1)]
            for i in range(n):
                if i == double_edge_ind:
                    continue
                u, v = E[i]
                G[u].append(v)
            if self.isDag(G, n):
                return E[double_edge_ind]
            else:
                return second_double_edge
        else:
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


    def isDag(self, G, n):
        vis = [False] * (n + 1)
        stack = []

        def toposort(u):
            for v in G[u]:
                if not vis[v]:
                    vis[v] = True
                    toposort(v)
            stack.append(u)

        def dfs(u):
            for v in G[u]:
                if not vis[v]:
                    vis[v] = True
                    dfs(v)

        for u in range(1, n + 1):
            if not vis[u]:
                toposort(u)
        vis = [False] * (n + 1)
        vis[stack[-1]] = True
        dfs(stack[-1])
        return not (False in vis[1:])

