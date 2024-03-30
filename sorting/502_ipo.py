import bisect
import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        arr = [(capital[i], profits[i], i) for i in range(n)]
        arr.sort()
        low = bisect.bisect_right(arr, w, key=lambda x: x[0])
        heap = [-x[1] for x in arr[:low]]
        heapq.heapify(heap)
        for _ in range(k):
            if len(heap) == 0:
                break
            w += -heapq.heappop(heap)
            high = bisect.bisect_right(arr, w, lo=low, key=lambda x: x[0])
            for i in range(low, high):
                heapq.heappush(heap, -arr[i][1])
            low = high
        return w
