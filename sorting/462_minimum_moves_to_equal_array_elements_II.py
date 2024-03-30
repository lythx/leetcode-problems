from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        eq_ind = n // 2
        flag = True
        while flag:
            flag = False
            greater_count = 0
            lesser_count = 0
            for x in nums:
                if x > nums[eq_ind]:
                    greater_count += 1
                elif x < nums[eq_ind]:
                    lesser_count += 1
            if greater_count > n // 2:
                eq_ind += 1
                flag = True
            elif lesser_count > n // 2:
                eq_ind -= 1
                flag = True
        return sum([abs(x - nums[eq_ind]) for x in nums])