from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, E: List[List[int]]) -> List[int]:
        G = [[] for _ in range(n)]
        for u, v in E:
            G[u].append(v)
            G[v].append(u)
        desc = [-1] * n
        distsum = [-1] * n
        parent = [0] * n

        def count_descendants(u, d):
            s = 0
            for v in G[u]:
                if desc[v] == -1:
                    parent[v] = u
                    desc[v] = 0
                    s += count_descendants(v, d + 1) + 1
                    distsum[0] += d + 1
            desc[u] = s
            return s

        desc[0] = 0
        distsum[0] = 0
        count_descendants(0, 0)

        def sum_dfs(u):
            for v in G[u]:
                if distsum[v] == -1:
                    d = desc[v]
                    s = distsum[u]
                    distsum[v] = s + n - 2 * d - 2
                    sum_dfs(v)

        sum_dfs(0)
        return distsum
