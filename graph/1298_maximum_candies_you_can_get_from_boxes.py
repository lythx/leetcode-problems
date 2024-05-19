from typing import List
from collections import deque


class Solution:
    def maxCandies(self, open: List[int], candies: List[int], G1: List[List[int]], G2: List[List[int]], initial: List[int]) -> int:
        q = deque()
        for u in initial:
            q.append(u)
        changed = True
        ans = 0
        while len(q) != 0 and changed:
            changed = False
            for _ in range(len(q)):
                u = q.popleft()
                if candies[u] == -1:
                    continue
                if not open[u]:
                    q.append(u)
                    continue
                changed = True
                ans += candies[u]
                candies[u] = -1
                for v in G1[u]:
                    if open[v] == 0:
                        open[v] = 1
                for v in G2[u]:
                    q.append(v)
        return ans
