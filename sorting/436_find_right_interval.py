import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = [(x[0], i) for i, x in enumerate(intervals)]
        ends = [(x[1], i) for i, x in enumerate(intervals)]
        starts.sort()
        ends.sort()
        ans = [-1] * n
        low = 0
        for i in range(n):
            low = bisect.bisect_left(starts, ends[i][0], low, key=lambda x: x[0])
            if low >= n:
                return ans
            ans[ends[i][1]] = starts[low][1]
        return ans



