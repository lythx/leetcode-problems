import heapq
from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        count = 0
        heap = [(x, i) for i, x in enumerate(arr)]
        heapq.heapify(heap)
        mx = -10000000
        while i < n:
            mn_ind = 0
            while heap:
                mn_ind = heapq.heappop(heap)[1]
                if i <= mn_ind:
                    break
            if i == 0:
                count += 1
            else:
                if arr[mn_ind] >= mx:
                    count += 1
            mx = max(mx, *arr[i:mn_ind + 1])
            i = mn_ind + 1
        return count