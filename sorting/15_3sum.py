class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        triplets = []
        nums.sort()
        i = 0
        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    j = left + 1
                    while j <= right and nums[j] == nums[left]:
                        j += 1
                    k = right - 1
                    while k >= left and nums[k] == nums[right]:
                        k -= 1
                    left = j
                    right = k
        return triplets
