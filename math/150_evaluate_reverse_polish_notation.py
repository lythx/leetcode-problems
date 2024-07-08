class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        add = lambda x, y: x + y
        subtract = lambda x, y: x - y
        multiply = lambda x, y: x * y
        divide = lambda x, y: (abs(x) // abs(y)) * (1 if (x > 0) == (y > 0) else -1)
        functions = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
        }
        num_stack = []
        for token in tokens:
            if token not in functions:
                num_stack.append(int(token))
                continue
            y = num_stack.pop()
            x = num_stack.pop()
            res = functions[token](x, y)
            num_stack.append(res)
        return num_stack.pop()

