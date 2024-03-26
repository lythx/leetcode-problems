from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        cur_end = points[0][1]
        arrows = 0
        for i in range(1, n):
            cur_end = min(cur_end, points[i][1])
            if points[i][0] > cur_end:
                arrows += 1
                cur_end = points[i][1]
        return arrows + 1



print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))