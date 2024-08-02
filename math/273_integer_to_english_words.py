class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = [None, "One", "Two", "Three", "Four", "Five",
                "Six", "Seven", "Eight", "Nine"]
        ten_to_nineteen = ["Ten", "Eleven", "Twelve", "Thirteen",
                           "Fourteen", "Fifteen", "Sixteen",
                           "Seventeen", "Eighteen", "Nineteen"]
        tens = [None, None, "Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]
        names = [" ", " Thousand ", " Million ", " Billion "]
        i = 0
        ans = ""
        while num != 0:
            arr = []
            num, chunk = divmod(num, 1000)
            if chunk == 0:
                i += 1
                continue
            hundreds, chunk = divmod(chunk, 100)
            if hundreds > 0:
                arr.append(ones[hundreds])
                arr.append("Hundred")
            if 10 <= chunk <= 19:
                arr.append(ten_to_nineteen[chunk - 10])
            else:
                tens_digit, chunk = divmod(chunk, 10)
                if tens_digit >= 2:
                    arr.append(tens[tens_digit])
                if chunk >= 1:
                    arr.append(ones[chunk])
            ans = " ".join(arr) + names[i] + ans
            i += 1

        return ans.strip()
