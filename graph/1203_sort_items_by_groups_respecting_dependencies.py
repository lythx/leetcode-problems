from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], G: List[List[int]]) -> List[int]:
        visited = [0] * n
        sorted_groups = [[] for _ in range(m)]

        def group_sort(u, g):
            for v in G[u]:
                if group[v] == g:
                    if visited[v] == 1:
                        return False
                    if visited[v] == 2:
                        continue
                    visited[v] = 1
                    if not group_sort(v, g):
                        return False
                    visited[v] = 2
            sorted_groups[g].append(u)
            return True

        for u in range(n):
            if visited[u] == 0 and group[u] != -1:
                visited[u] = 1
                if not group_sort(u, group[u]):
                    return []
                visited[u] = 2

        vmap = [u for u in range(n)]
        for g in sorted_groups:
            for u in g[1:]:
                G[g[0]] += G[u]
                vmap[u] = g[0]
        visited = [0] * n
        stack = []

        def graph_sort(u):
            for v in G[vmap[u]]:
                if vmap[v] == vmap[u]:
                    continue
                if visited[vmap[v]] == 1:
                    return False
                if visited[vmap[v]] == 2:
                    continue
                visited[vmap[v]] = 1
                if not graph_sort(vmap[v]):
                    return False
                visited[vmap[v]] = 2
            stack.append(vmap[u])
            return True

        for u in range(n):
            if visited[vmap[u]] == 0:
                visited[vmap[u]] = 1
                if not graph_sort(vmap[u]):
                    return []
                visited[vmap[u]] = 2

        ans = []
        for x in stack:
            if group[x] == -1:
                ans.append(x)
            else:
                ans += sorted_groups[group[x]]
        return ans
