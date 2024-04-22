from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        new_leaves = set()
        node_count = n
        while node_count > 2:
            for leaf in leaves:
                v = adj[leaf].pop()
                adj[v].remove(leaf)
                if len(adj[v]) == 1:
                    new_leaves.add(v)
            node_count -= len(leaves)
            leaves = list(new_leaves)
            new_leaves = set()
        return leaves
