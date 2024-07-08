from string import ascii_uppercase

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(ascii_uppercase)
        index = {x: i + 1 for i, x in enumerate(ascii_uppercase)}
        p = 1
        ans = 0
        for c in reversed(columnTitle):
            ans += index[c] * p
            p *= n
        return ans
