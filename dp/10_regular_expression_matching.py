class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        i = 0

        while i < m - 4:
            if p[i] == p[i + 2] and p[i + 1] == p[i + 3] == '*':
                p = p[i:i+2] + p[i+4:]
                m -= 2

        def test(s_char, p_char):
            if p_char == '.':
                return True
            return s_char == p_char

        # i - s index, j - p index
        def match(i, j):
            if i == n and j == m:
                return True
            if j == m:
                return False
            if j + 1 < m and p[j + 1] == '*':
                j += 1
            if p[j] == '*':
                if i < n and test(s[i], p[j - 1]):
                    if match(i + 1, j):
                        return True
                if match(i, j + 1):
                    return True
            return i < n and test(s[i], p[j]) and match(i + 1, j + 1)

        return match(0, 0)