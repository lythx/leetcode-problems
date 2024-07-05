from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for row in range(1, numRows):
            arr = [0] * (row + 1)
            prev = ans[-1]
            for i in range(row + 1):
                if i > 0:
                    arr[i] += prev[i - 1]
                if i < row:
                    arr[i] += prev[i]
            ans.append(arr)
        return ans
