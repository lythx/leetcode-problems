from math import isqrt

class Solution:
    def numSquares(self, n: int) -> int:
        sq_n = isqrt(n)
        squares = []
        for i in reversed(range(1, sq_n + 1)):
            squares.append(i*i)
        memo = [-2] * n

        def dfs(sq_sum):
            if sq_sum > n:
                return -1
            if sq_sum == n:
                return 0
            if memo[sq_sum] != -2:
                return memo[sq_sum]
            min_res = -1
            for sq in squares:
                res = dfs(sq + sq_sum)
                if res != -1:
                    if res < min_res or min_res == -1:
                        min_res = res
            memo[sq_sum] = min_res + 1
            return min_res + 1

        dfs(0)
        return memo[0]
