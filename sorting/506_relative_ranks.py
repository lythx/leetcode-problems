from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        arr = sorted(range(n), key=lambda i: -score[i])
        ans = [0] * n
        ans[arr[0]] = "Gold Medal"
        if n == 1:
            return ans
        ans[arr[1]] = "Silver Medal"
        if n == 2:
            return ans
        ans[arr[2]] = "Bronze Medal"
        for i in range(3, n):
            ans[arr[i]] = str(i + 1)
        return ans