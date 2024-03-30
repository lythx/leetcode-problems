from typing import List
import bisect

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        k = len(s)
        g.sort()
        s.sort()
        low = 0
        count = 0
        for greed in g:
            low = bisect.bisect_left(s, greed, low)
            if low == k:
                break
            low += 1
            count += 1
        return count