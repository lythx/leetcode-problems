class Solution:
    def nthUglyNumber(self, n: int) -> int:
        next2 = 0
        next3 = 0
        next5 = 0
        arr = [1]
        for i in range(1, n):
            val2 = arr[next2] * 2
            if val2 == arr[-1]:
                next2 += 1
                val2 = arr[next2] * 2
            val3 = arr[next3] * 3
            if val3 == arr[-1]:
                next3 += 1
                val3 = arr[next3] * 3
            val5 = arr[next5] * 5
            if val5 == arr[-1]:
                next5 += 1
                val5 = arr[next5] * 5
            if val2 <= val3 and val2 <= val5:
                arr.append(val2)
                next2 += 1
            elif val3 <= val5:
                arr.append(val3)
                next3 += 1
            else:
                arr.append(val5)
                next5 += 1
        return arr[-1]
