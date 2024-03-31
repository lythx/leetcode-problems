class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (right + left) // 2
            if self.count_pairs(nums, mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

    def count_pairs(self, nums, d):
        n = len(nums)
        count = j = 0
        for i in range(n):
            while j < n and nums[j] - nums[i] <= d:
                j += 1
            count += j - i - 1
        return count