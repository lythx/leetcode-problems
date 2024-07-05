class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low < high:
            mid = (high - low) // 2 + low + 1
            if mid*mid < x:
                low = mid
            elif x < mid*mid:
                high = mid - 1
            else:
                return mid
        return low
