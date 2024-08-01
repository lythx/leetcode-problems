from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for x in nums:
            index = bisect_left(dp, x)
            if index == len(dp):
                dp.append(x)
            else:
                dp[index] = x
        return len(dp)
