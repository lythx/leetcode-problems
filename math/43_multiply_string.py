class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        ans = [0] * (n1 + n2)
        for i in reversed(range(1, n1 + 1)):
            rem = 0
            a = int(num1[i - 1])
            for j in reversed(range(n2)):
                x = a * int(num2[j]) + rem + ans[i + j]
                ans[i + j] = x % 10
                rem = x // 10
            j = -1
            while rem > 0:
                x = rem + ans[i + j]
                ans[i + j] = x % 10
                rem = x // 10
                j -= 1
        return ''.join([str(x) for x in ans]).lstrip('0')

