import random
import bisect
from typing import List


class Solution:
    def __init__(self, n, blacklist):
        self.k = len(blacklist)
        self.bl = sorted(blacklist)
        self.n = n - self.k
        self.mp = [0] * self.k
        j = 0
        for i in range(self.k):
            if self.bl[i] < self.n:
                while j + self.n in self.bl:
                    j += 1
                self.mp[i] = j + self.n
                j += 1

    def pick(self):
        r = random.randint(0, self.n - 1)
        ind = bisect.bisect_left(self.bl, r)
        if ind < self.k and self.bl[ind] == r:
            return self.mp[ind]
        return r


