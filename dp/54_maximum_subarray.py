import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = -math.inf
        for i, x in enumerate(nums):
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
            cur_sum = max(cur_sum, 0)
        return max_sum
