from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def dfs(p, i=0):
            if not p:
                return
            if i >= len(ans):
                ans.append([p.val])
            else:
                ans[i].append(p.val)
            dfs(p.left, i + 1)
            dfs(p.right, i + 1)

        dfs(root)
        return ans
