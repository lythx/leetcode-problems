from typing import List


class Solution:

    memo = {}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.memo:
            return self.memo[expression]
        n = len(expression)
        if n <= 2:
            return [int(expression)]

        def evaluate(x, y, op):
            if op == '+':
                return x + y
            if op == '-':
                return x - y
            return x * y

        ans = []
        last_num = None
        for i, c in enumerate(expression):
            if not (c == '+' or c == '-' or c == '*'):
                if last_num is None:
                    last_num = int(c)
                else:
                    last_num = last_num * 10 + int(c)
                continue
            last_num = None
            left = self.diffWaysToCompute(expression[0:i])
            right = self.diffWaysToCompute(expression[i+1:n])
            for x in left:
                for y in right:
                    ans.append(evaluate(x, y, c))
        self.memo[expression] = ans
        return ans
            