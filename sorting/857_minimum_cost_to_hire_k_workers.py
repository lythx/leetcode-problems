import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        arr = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)], reverse=True)
        heap = [(x[1], i) for i, x in enumerate(arr)]
        heapq.heapify(heap)
        in_sum = [False] * n
        s = 0
        for i in range(k - 1):
            qual, ind = heapq.heappop(heap)
            s += qual
            in_sum[ind] = True
        mn = 100000000000000000
        for i in range(n - k + 1):
            ratio, qual = arr[i]
            if in_sum[i]:
                while True:
                    new_qual, new_ind = heapq.heappop(heap)
                    if new_ind > i:
                        break
                s += new_qual - qual
                in_sum[new_ind] = True
            cost = (s + qual) * ratio
            if cost < mn:
                mn = cost
        return mn

