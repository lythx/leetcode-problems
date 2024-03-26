from string import ascii_letters

class Solution:
    def frequencySort(self, s: str) -> str:
        alp = ascii_letters + "".join([str(i) for i in range(10)])
        k = len(alp)
        counts = [(0, i) for i in range(k)]
        for c in s:
            counts[alp.index(c)][0] += 1
        counts.sort()
        ans = ""
        for count, idx in counts:
            ans += alp[idx] * count
        return ans
