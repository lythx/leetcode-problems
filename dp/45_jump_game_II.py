from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        last_jump = 0
        cur_jump = 0
        jump_count = 0
        for i, x in enumerate(nums):
            if last_jump < i:
                jump_count += 1
                last_jump = cur_jump
            if i + x > cur_jump:
                cur_jump = i + x
                if cur_jump >= n - 1:
                    return jump_count + 1
        return -1
