class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        arr = [0] * n
        day = 60 * 24
        for i, p in enumerate(timePoints):
            arr[i] = int(p[:2]) * 60 + int(p[3:])
        arr.sort()
        mn = arr[1] - arr[0]
        for i in range(2, n):
            if arr[i] - arr[i - 1] < mn:
                mn = arr[i] - arr[i - 1]
        if day - arr[-1] + arr[0] < mn:
            mn = day - arr[-1] + arr[0]
        return mn