import bisect
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        cur_end = intervals[0][1]
        count = 0
        for i in range(1, n):
            if intervals[i][0] >= cur_end:
                cur_end = intervals[i][1]
            else:
                cur_end = min(cur_end, intervals[i][1])
                count += 1
        return count