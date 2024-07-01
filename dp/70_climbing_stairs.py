from math import sqrt

class Solution:
    def climbStairs(self, n: int) -> int:
        sq5 = sqrt(5)
        return round((1 / sq5) * pow((1 + sq5) / 2, n + 1) - \
                     (1 / sq5) * pow((1 - sq5) / 2, n + 1))
