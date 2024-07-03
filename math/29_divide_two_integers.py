class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
            max_int = (1 << 31) - 1
        else:
            sign = -1
            max_int = 1 << 31
        p = abs(dividend)
        q = abs(divisor)
        ans = 0
        while p >= q:
            product = q
            count = -1
            while p - product >= 0:
                product <<= 1
                count += 1
            quot = 1 << count
            if ans > max_int - quot:
                return sign * max_int
            ans += quot
            product >>= 1
            p -= product
        return sign * ans