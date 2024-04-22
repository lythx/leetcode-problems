from typing import List
from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        m = len(equations)
        G = {}
        for i in range(m):
            a, b = equations[i]
            if G.get(a):
                G[a].append((b, values[i]))
            else:
                G[a] = [(b, values[i])]
            if G.get(b):
                G[b].append((a, 1 / values[i]))
            else:
                G[b] = [(a, 1 / values[i])]

        ans = [-1] * len(queries)
        for i in range(len(queries)):
            c, d = queries[i]
            if G.get(c) is None or G.get(d) is None:
                continue
            vis = {v: False for v in G}
            parent = {v: None for v in G}
            que = deque()
            que.append((c, 1))
            vis[c] = True
            while len(que) != 0:
                u = que.pop()
                if u[0] == d:
                    ans[i] = u[1]
                    break
                if G.get(u[0]) is None:
                    continue
                for v in G[u[0]]:
                    if vis[v[0]]:
                        continue
                    vis[v[0]] = True
                    parent[v[0]] = u
                    que.append(v)
            if ans[i] != -1:
                v = d
                while parent.get(v) is not None:
                    ans[i] *= parent[v][1]
                    v = parent[v][0]
        return ans
