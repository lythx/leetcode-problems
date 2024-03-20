class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
            if nums[high] == 2:
                high -= 1
            elif nums[low] != 2:
                low += 1
            else:
                nums[high], nums[low] = nums[low], nums[high]
                low += 1
                high -= 1
        if nums[high] == 2:
            high -= 1
        low = 0
        while low < high:
            if nums[high] == 1:
                high -= 1
            elif nums[low] != 1:
                low += 1
            else:
                nums[high], nums[low] = nums[low], nums[high]
                low += 1
                high -= 1

