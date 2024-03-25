import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        arr = []
        for e in envelopes:
            ind = bisect.bisect_left(arr, e[1])
            if ind == len(arr):
                arr.append(e[1])
            else:
                arr[ind] = e[1]
        return len(arr)
