class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        while n != 1 and n not in memo:
            memo.add(n)
            new_n = 0
            while n > 0:
                m = n % 10
                new_n += m*m
                n //= 10
            n = new_n
        return n == 1
