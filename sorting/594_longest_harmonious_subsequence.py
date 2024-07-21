from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        low = 0
        high = 0
        while high < n and nums[high] - nums[low] != 1:
            if nums[high] == nums[low]:
                high += 1
            else:
                low += 1
        if high == n or nums[high] - nums[low] != 1:
            return 0
        max_len = high - low + 1
        while high < n:
            if nums[high] - nums[low] == 0:
                high += 1
            elif nums[high] - nums[low] == 1:
                max_len = max(max_len, high - low + 1)
                high += 1
            else:
                low += 1
        return max_len
