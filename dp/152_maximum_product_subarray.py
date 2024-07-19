from math import inf
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = -inf
        cur_pos = -inf
        cur_neg = inf
        for num in nums:
            if num > 0:
                cur_pos = max(cur_pos * num, num)
                cur_neg *= num
            elif num < 0:
                old_neg = cur_neg
                cur_neg = min(cur_pos * num, num)
                cur_pos = old_neg * num
            else:
                cur_pos = cur_neg = 0
            if cur_pos > max_prod:
                max_prod = cur_pos
            elif cur_neg != inf and cur_neg > max_prod:
                max_prod = cur_neg
        return max_prod

