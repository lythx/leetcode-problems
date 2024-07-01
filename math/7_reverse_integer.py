class Solution:
    def reverse(self, x: int) -> int:
        sign = x // abs(x)
        x = abs(x)
        ans = 0
        mx = 2**31 - 1
        while x > 0:
            m = x % 10
            if ans > (mx - m) / 10:
                return 0
            ans = ans * 10 + m
            x //= 10
        return sign * ans
        