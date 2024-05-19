from typing import List
from collections import deque

class Solution:
    def watchedVideosByFriends(self, vids: List[List[str]], G: List[List[int]], id: int, level: int) -> List[str]:
        n = len(G)
        q = deque()
        q.append(id)
        visited = [False] * n
        step = 0
        while len(q) != 0 and step < level:
            for _ in range(len(q)):
                u = q.popleft()
                for v in G[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            step += 1
        freq = {}
        for _ in range(len(q)):
            u = q.popleft()
            print(u)
            for vid in vids[u]:
                if vid in freq:
                    freq[vid] += 1
                else:
                    freq[vid] = 1
        return [z[1] for z in sorted([(y, x) for x, y in freq.items()])]

a = Solution().watchedVideosByFriends([["A","B"],["C"],["B","C"],["D"]], [[1,2],[0,3],[0,3],[1,2]], 0, 2)
print(a)
