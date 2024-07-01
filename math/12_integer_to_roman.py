class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        while num >= 1000:
            num -= 1000
            ans += 'M'

        if num >= 900:
            num -= 900
            ans += 'CM'
        elif num >= 500:
            num -= 500
            ans += 'D'
        elif num >= 400:
            num -= 400
            ans += 'CD'
        while num >= 100:
            num -= 100
            ans += 'C'

        if num >= 90:
            num -= 90
            ans += 'XC'
        if num >= 50:
            num -= 50
            ans += 'L'
        elif num >= 40:
            num -= 40
            ans += 'XL'
        while num >= 10:
            num -= 10
            ans += 'X'

        if num >= 9:
            num -= 9
            ans += 'IX'
        if num >= 5:
            num -= 5
            ans += 'V'
        elif num >= 4:
            num -= 4
            ans += 'IV'
        while num >= 1:
            num -= 1
            ans += 'I'

        return ans


