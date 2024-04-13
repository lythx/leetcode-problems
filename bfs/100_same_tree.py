# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def step(p, q):
            if not p and not q:
                return True
            if p and q:
                if p.val != q.val:
                    return False
                if not step(p.left, q.left):
                    return False
                return step(p.right, q.right)
            return False
        return step(p, q)


