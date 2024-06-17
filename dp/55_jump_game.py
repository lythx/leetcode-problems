from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        last_jump = 0
        cur_jump = 0
        for i, x in enumerate(nums):
            if last_jump < i:
                if cur_jump < i:
                    break
                last_jump = cur_jump
            if i + x > cur_jump:
                cur_jump = i + x
                if cur_jump >= n - 1:
                    return True
        return False