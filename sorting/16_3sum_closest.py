class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        closest = float('inf')
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    print(s)
                    return s
        print(closest)
        return closest
