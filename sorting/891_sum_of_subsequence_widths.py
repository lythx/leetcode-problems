from typing import List
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        s = 0
        m = pow(10, 9) + 7
        for i in range(n):
            s = (s + nums[i] * pow(2, i, m)) % m
            s = (s - nums[i] * pow(2, n - i - 1, m)) % m
        return s
