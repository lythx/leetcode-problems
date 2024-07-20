from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        last = nums[0]
        for num in nums[1:]:
            new_last = prev + num
            prev = last
            last = max(last, new_last)
        return max(prev, last)

