from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                low = i - 1
                break
        high = low
        for i in range(n - 1, low, -1):
            if nums[i] < nums[i - 1]:
                high = i + 1
                break
        if low == high:
            return 0
        arr = nums[low:high]
        mn = min(arr)
        mx = max(arr)
        while low >= 0 and nums[low] > mn:
            low -= 1
        low += 1
        while high <= n and nums[high - 1] < mx:
            high += 1
        high -= 1
        return high - low
