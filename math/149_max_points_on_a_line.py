from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mx = 0
        for i in range(n):
            x0, y0 = points[i]
            tan_count = {}
            y_axis_count = 0
            for x, y in points[(i + 1):]:
                if x == x0:
                    y_axis_count += 1
                    continue
                tan = (y - y0) / (x - x0)
                if tan in tan_count:
                    tan_count[tan] += 1
                else:
                    tan_count[tan] = 1
            mx = max(mx, y_axis_count, *tan_count.values())
        return mx + 1

