class Solution:
    def romanToInt(self, s: str) -> int:
        double_map = {
            'CM': 900,
            'CD': 400,
            'XC': 90,
            'XL': 40,
            'IX': 9,
            'IV': 4
        }
        single_map = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        n = len(s)
        ans = 0
        i = 0
        while i < n - 1:
            if s[i] + s[i + 1] in double_map:
                ans += double_map[s[i] + s[i + 1]]
                i += 2
            else:
                ans += single_map[s[i]]
                i += 1
        if i < n:
            ans += single_map[s[i]]
        return ans
