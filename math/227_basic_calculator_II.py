class Solution:
    def calculate(self, s: str) -> int:
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: (1 if (x > 0) == (y > 0) else -1) * int(abs(x) / abs(y))
        }


        s = [c for c in s if c != " "]
        nums = []
        ops = []
        num = 0
        i = 0
        while i < len(s):
            if s[i] in operations:
                nums.append(num)
                ops.append(s[i])
                num = 0
            else:
                num = num * 10 + int(s[i])
            i += 1
        nums.append(num)

        i = 0
        while i < len(ops):
            if ops[i] != '*' and ops[i] != '/':
                i += 1
                continue
            x = nums[i]
            y = nums[i + 1]
            result = operations[ops[i]](x, y)
            ops.pop(i)
            nums.pop(i)
            nums[i] = result

        for i in range(len(ops)):
            x = nums[i]
            y = nums[i + 1]
            result = operations[ops[i]](x, y)
            nums[i + 1] = result
        return nums[-1]
