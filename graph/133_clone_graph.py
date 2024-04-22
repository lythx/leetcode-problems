
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        q = deque()
        visited = dict()
        q.append(node)
        copy_root = Node(val=node.val)
        copy_dict = {node.val: copy_root}
        while len(q) != 0:
            for _ in range(len(q)):
                node = q.pop()
                copy_node = copy_dict.get(node.val)
                if visited.get(node.val):
                    continue
                for n in node.neighbors:
                    q.append(n)
                    n_copy = copy_dict.get(n.val)
                    if not n_copy:
                        n_copy = Node(val=n.val)
                        copy_dict[n.val] = n_copy
                    copy_node.neighbors.append(n_copy)
                visited[node.val] = True
        return copy_root
