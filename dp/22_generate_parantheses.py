from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        # s - parentheses string, p - open-closed parentheses count
        def step(s, p):
            if len(s) == 2 * n:
                if p == 0:
                    ans.append(s)
                return
            if p != 0:
                step(s + ')', p - 1)
            step(s + '(', p + 1)

        step('', 0)
        return ans