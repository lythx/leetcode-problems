from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        k = len(heaters)
        houses.sort()
        heaters.sort()
        if k == 1:
            return max(abs(houses[0] - heaters[0]), abs(houses[-1] - heaters[0]))
        radius = 0
        j = 0
        for h in houses:
            while j < k - 2 and h > heaters[j + 1]:
                j += 1
            radius = max(radius, min(abs(h - heaters[j]), abs(h - heaters[j + 1])))
        return radius