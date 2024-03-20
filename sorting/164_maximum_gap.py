class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        mx = -1
        for i in range(1, n):
            diff = abs(nums[i] - nums[i - 1])
            if diff > mx:
                mx = diff
        return mx
