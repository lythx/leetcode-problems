class Solution:
    def countDigitOne(self, n: int) -> int:
        one_count = 0
        p = 1
        while p <= n:
            a, b = divmod(n, p)
            if a % 10 == 1:
                one_count += (a // 10) * p + b + 1
            elif a % 10 == 0:
                one_count += (a // 10) * p
            else:
                one_count += (a // 10 + 1) * p
            p *= 10
        return one_count
