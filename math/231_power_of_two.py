class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return 1_073_741_824 % n == 0
