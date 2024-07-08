# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = root.val

        def step(p):
            nonlocal mx
            if p is None:
                return 0
            left = max(step(p.left), 0)
            right = max(step(p.right), 0)
            mx = max(mx, left + p.val + right)
            return max(left + p.val, right + p.val, 0)

        step(root)
        return mx