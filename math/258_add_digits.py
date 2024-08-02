class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return ((num - 1) % 9) + 1



for i in range(1000):
    print(i, Solution().addDigits(i))