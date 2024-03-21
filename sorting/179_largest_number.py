import functools
import math


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        key = functools.cmp_to_key(self.compare)
        arr = sorted(nums, key=key)
        s = ""
        for x in arr:
            s += str(x)
        if s[0] == "0":
            return "0"
        return s

    def compare(self, a, b):
        if a == 0:
            return 1
        if b == 0:
            return -1
        pa = 10**int(math.log10(a) + 1)
        pb = 10**int(math.log10(b) + 1)
        if a * pb + b > a + b * pa:
            return -1
        else:
            return 1

