from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        m = len(tickets)
        G = {}
        for u, v in tickets:
            if G.get(u) is not None:
                G[u].append(v)
            else:
                G[u] = [v]
            if G.get(v) is None:
                G[v] = []
        for v, adj in G.items():
            adj.sort(reverse=True)
        stack = ['JFK']
        ans = []
        while stack:
            if G[stack[-1]]:
                stack.append(G[stack[-1]].pop())
            else:
                ans.append(stack.pop())
        return reversed(ans)

