from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = [[None] * (n + 2) for _ in range(n + 2)]
        return self.generate_subtrees(1, n + 1, memo)

    def generate_subtrees(self, low, high, memo):
        if memo[low][high] is not None:
            return memo[low][high]
        if low == high:
            return [None]
        subtrees = []
        for i in range(low, high):
            left = self.generate_subtrees(low, i, memo)
            right = self.generate_subtrees(i + 1, high, memo)
            for l_tree in left:
                for r_tree in right:
                    tree = TreeNode(i, l_tree, r_tree)
                    subtrees.append(tree)
        memo[low][high] = subtrees
        return subtrees
