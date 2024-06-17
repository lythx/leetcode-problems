class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def test(s_str, p_str):
            if len(s_str) != len(p_str):
                return False
            for i, c in enumerate(p_str):
                if c != '?' and c != s_str[i]:
                    return False
            return True

        n = len(s)
        m = len(p)
        if '*' not in p:
            return test(s, p)
        start = p.index('*')
        if start > n or (not test(s[:start], p[:start])):
            return False
        end = m - p.rindex('*') - 1
        if (end > n or (not test(s[max(n-end, start):], p[m-end:]))):
            return False
        patterns = [x for x in p[start:m-end].split('*') if x != '']
        i = start
        for pt in patterns:
            k = len(pt)
            found_match = False
            while i + k <= n - end:
                if test(s[i:i+k], pt):
                    found_match = True
                    break
                i += 1
            if not found_match:
                return False
            i += k
        return True