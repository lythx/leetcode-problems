from string import ascii_uppercase

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = len(ascii_uppercase)
        ans = ''
        while columnNumber > 0:
            ans = ascii_uppercase[(columnNumber - 1) % n] + ans
            columnNumber = (columnNumber - 1) // n
        return ans
