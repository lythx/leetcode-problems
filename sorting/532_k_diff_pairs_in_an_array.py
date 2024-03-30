from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        low = 0
        high = 1
        ans = []
        while high < n:
            if nums[high] - nums[low] > k:
                low += 1
            elif nums[high] - nums[low] < k:
                high += 1
            else:
                if (nums[low], nums[high]) not in ans:
                    ans.append((nums[low], nums[high]))
                low += 1
            if low == high:
                high += 1
        return len(ans)