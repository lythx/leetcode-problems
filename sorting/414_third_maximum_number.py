from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        mx = []
        for i in range(3):
            cur_mx = -2**32
            for x in nums:
                if x > cur_mx and x not in mx:
                    cur_mx = x
            if cur_mx == -2**32:
                return mx[0]
            mx.append(cur_mx)
        return mx[2]