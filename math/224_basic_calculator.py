class Solution:
    def calculate(self, s: str) -> int:
        return self._calculate(s.replace(' ', '') + ')', 0)[0]

    def _calculate(self, s: str, start: int) -> tuple[int, int]:
        last_op = '+'
        last_num = 0
        i = start
        while s[i] != ')':
            if s[i] == '+' or s[i] == '-':
                last_op = s[i]
                i += 1
                continue

            if s[i] == '(':
                num, ind = self._calculate(s, i + 1)
                i = ind
            else:
                j = i + 1
                while s[j] != '+' and s[j] != '-' and s[j] != ')':
                    j += 1
                num = int(s[i:j])
                i = j - 1

            if last_op == '+':
                last_num += num
            else:
                last_num -= num
            i += 1

        return last_num, i