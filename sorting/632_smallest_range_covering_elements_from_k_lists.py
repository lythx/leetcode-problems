import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        heap = [(x[0], i, 0) for i, x in enumerate(nums)]
        heapq.heapify(heap)
        mx = max(heap, key=lambda x: x[0])[0]
        mn_range = [heap[0][0], mx]
        mn_size = mn_range[1] - mn_range[0]
        while True:
            mn = heap[0]
            if mn[2] + 1 == len(nums[mn[1]]):
                break
            new_el = nums[mn[1]][mn[2] + 1]
            if new_el > mx:
                mx = new_el
            heapq.heapreplace(heap, (new_el, mn[1], mn[2] + 1))
            if mx - heap[0][0] < mn_size:
                mn_range = [heap[0][0], mx]
                mn_size = mn_range[1] - mn_range[0]
        return mn_range
