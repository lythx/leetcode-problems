class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 1
        leader = nums[0]
        for i in range(1, n):
            if nums[i] != leader:
                count -= 1
                if count == 0:
                    leader = nums[i]
                    count = 1
            else:
                count += 1
        return leader