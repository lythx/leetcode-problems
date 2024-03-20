class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        quads = []
        nums.sort()
        i = 0
        for i in range(n - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s > target:
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        quads.append([nums[i], nums[j], nums[left], nums[right]])
                        k = left + 1
                        while k <= right and nums[k] == nums[left]:
                            k += 1
                        m = right - 1
                        while m >= left and nums[m] == nums[right]:
                            m -= 1
                        left = k
                        right = m
        return quads
