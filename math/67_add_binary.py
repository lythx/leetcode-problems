class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        i = len(a) - 1
        j = len(b) - 1
        c = []
        rem = 0
        while j >= 0:
            rem += int(a[i]) + int(b[j])
            c.append(str(rem % 2))
            rem //= 2
            i -= 1
            j -= 1
        while i >= 0:
            rem += int(a[i])
            c.append(str(rem % 2))
            rem //= 2
            i -= 1
        while rem > 0:
            c.append(str(rem % 2))
            rem //= 2
        return ''.join(reversed([str(x) for x in c]))
