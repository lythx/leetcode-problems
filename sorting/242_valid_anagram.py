class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        oa = ord('a')
        counts = [0]*(ord('z') - oa + 1)
        for c in s:
            counts[ord(c) - oa] += 1
        for c in t:
            counts[ord(c) - oa] -= 1
            if counts[ord(c) - oa] == -1:
                return False
        return True
