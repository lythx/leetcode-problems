
class Solution:

    def numTrees(self, n: int) -> int:
        memo = [[None] * (n + 2) for _ in range(n + 2)]
        return self.count_subtrees(1, n + 1, memo)

    def count_subtrees(self, low, high, memo):
        if memo[low][high] is not None:
            return memo[low][high]
        if low == high:
            return [None]
        count = 0
        for i in range(low, high):
            left = self.count_subtrees(low, i, memo)
            right = self.count_subtrees(i + 1, high, memo)
            count += left * right
        memo[low][high] = count
        return count
