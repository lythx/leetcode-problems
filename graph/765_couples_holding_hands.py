from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        arr = [y[0] for y in sorted(enumerate(row), key=lambda x: x[1])]
        G = [[] for _ in range(n)]
        for i in range(0, 2 * n, 2):
            G[arr[i] // 2].append(arr[i + 1] // 2)
            G[arr[i + 1] // 2].append(arr[i] // 2)
        vis = [False] * n
        def dfs(u, start):
            for v in G[u]:
                if not vis[v]:
                    vis[v] = True
                    return dfs(v, start) + 1
            return 1

        count = 0
        for u in reversed(range(n)):
            if not vis[u]:
                vis[u] = True
                count += dfs(u, u) - 1
        return count


print(Solution().minSwapsCouples([5,3,4,2,1,0]))