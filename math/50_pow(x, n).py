class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self._pow(x, -n)
        return self._pow(x, n)

    def _pow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        p = self.myPow(x, n // 2)
        ans = p * p
        if n % 2 == 1:
            ans *= x
        return ans

