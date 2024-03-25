class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = len(s)
        counts = [0] * (ord('z') - ord('a') + 1)
        for c in t:
            counts[ord(c) - ord('a')] += 1
        for c in s:
            counts[ord(c) - ord('a')] -= 1
        for i in range(len(counts)):
            if counts[i] == 1:
                return chr(ord('a') + i)
        return ""