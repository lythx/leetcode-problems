from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_h = max(height)
        all_sum = 0
        i = 0
        cur_max = 0
        while height[i] != max_h:
            if cur_max < height[i]:
                cur_max = height[i]
            all_sum += cur_max
            i += 1
        j = n - 1
        cur_max = 0
        while height[j] != max_h:
            if cur_max < height[j]:
                cur_max = height[j]
            all_sum += cur_max
            j -= 1
        return all_sum + (j - i + 1) * max_h - sum(height)

