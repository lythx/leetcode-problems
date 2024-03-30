from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        n = len(strs)
        strs.sort(key=len, reverse=True)
        for i in range(n):
            s = strs[i]
            k = len(s)
            mask = 2**k
            while mask >= 0:
                seq = ""
                j = 0
                m = mask
                while j < k and m > 0:
                    if m % 2 == 0:
                        seq += s[j]
                    m /= 2
                    j += 1
                if all([(not self.has_subseq(x, seq) or ind == i) for ind, x in enumerate(strs)]):
                    return len(seq)
                mask -= 1
        return -1


    def has_subseq(self, s, subseq):
        if len(s) < len(subseq):
            return False
        i = 0
        for j in range(len(subseq)):
            while i < len(s) and s[i] != subseq[j]:
                i += 1
            if i == len(s):
                return False
            i += 1
        return True




