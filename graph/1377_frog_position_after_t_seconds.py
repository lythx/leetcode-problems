from typing import List
from collections import deque

class Solution:
    def frogPosition(self, n: int, E: List[List[int]], t: int, target: int) -> float:
        G = [[] for _ in range(n + 1)]
        for u, v in E:
            G[u].append(v)
            G[v].append(u)
        visited = [False] * (n + 1)
        visited[1] = True
        q = deque()
        q.append((1, 1))
        ans = 0
        i = 0
        while len(q) != 0 and i < t:
            for _ in range(len(q)):
                u, p = q.popleft()
                print(u)
                options = 0
                for v in G[u]:
                    if not visited[v]:
                        options += 1
                if options == 0 and u == target:
                    ans += p
                elif options != 0:
                    new_p = p / options
                    for v in G[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append((v, new_p))
            i += 1

        for _ in range(len(q)):
            u, p = q.popleft()
            print(u, p)
            if u == target:
                ans += p
        print(ans)
        return ans

Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4)