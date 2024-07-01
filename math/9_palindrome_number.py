from math import log10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        digit_count = int(log10(x) + 1)
        p = 10**(digit_count - 1)
        for _ in range(digit_count // 2):
            if x // p != x % 10:
                return False
            x %= p
            x //= 10
            p //= 100
        return True
