from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        triplet_count = 0
        for i in reversed(range(n)):
            x = nums[i]
            low = 0
            high = i - 1
            while low < high:
                s = nums[low] + nums[high]
                if s > x:
                    triplet_count += high - low
                    high -= 1
                else:
                    low += 1
        return triplet_count
