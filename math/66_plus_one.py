from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 1
        i = len(digits) - 1
        while i >= 0 and rem != 0:
            rem += digits[i]
            digits[i] = rem % 10
            rem //= 10
            i -= 1
        if rem != 0:
            digits.insert(0, rem)
        return digits