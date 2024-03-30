from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        s = 0
        for i in range(0, n, 2):
            s += nums[i]
        return s