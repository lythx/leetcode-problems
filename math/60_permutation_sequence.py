from typing import List
from math import ceil, factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self._getPermutation(n, k, [x + 1 for x in range(n)], factorial(n - 1))

    def _getPermutation(self, n: int, k: int, arr: List[int], f: int) -> str:
        first = ceil(k / f) - 1
        remainder = k - first * f
        first_char = str(arr[first])
        arr.pop(first)
        if n == 1:
            return first_char
        return first_char + self._getPermutation(n - 1, remainder, arr, f // (n - 1))

a = Solution().getPermutation(2, 2)
print(a)
