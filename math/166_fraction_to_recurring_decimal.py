class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        sign = '' if (numerator > 0) == (denominator > 0) else '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        remainders = {}
        i = 0
        period_len = -1
        whole, n = divmod(numerator, denominator)
        n *= 10
        decimal = ''
        while n != 0:
            q, rem = divmod(n, denominator)
            if q == 0:
                n *= 10
                i += 1
                decimal += '0'
                continue
            decimal += str(q)
            if rem in remainders:
                period_len = i - remainders[rem]
                break
            remainders[rem] = i
            n = rem * 10
            i += 1
        if period_len != -1:
            return sign + str(whole) + '.' + decimal[:-period_len] + '(' + decimal[-period_len:] + ')'
        if len(decimal) == 0:
            return sign + str(whole)
        return sign + str(whole) + '.' + decimal