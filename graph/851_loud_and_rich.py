from typing import List


class Solution:
    def loudAndRich(self, E: List[List[int]], q: List[int]) -> List[int]:
        n = len(q)
        G = [[] for _ in range(n)]
        for u, v in E:
            G[v].append(u)
        ans = [-1] * n

        def dfs(u):
            ans[u] = u
            for v in G[u]:
                if ans[v] == -1:
                    dfs(v)
                if q[ans[v]] < q[ans[u]]:
                    ans[u] = ans[v]

        for u in range(n):
            if ans[u] == -1:
                dfs(u)

        return ans

