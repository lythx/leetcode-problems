from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev = 0
        last = nums[0]
        for num in nums[1:-1]:
            new_last = prev + num
            prev = last
            last = max(last, new_last)
        prev2 = 0
        last2 = nums[1]
        for num in nums[2:]:
            new_last = prev2 + num
            prev2 = last2
            last2 = max(last2, new_last)
        return max(prev, last, prev2, last2)

