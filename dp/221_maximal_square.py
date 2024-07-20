from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        hist = [0] * (n + 2)
        mx = 0

        for row in matrix:
            for i in range(n):
                if row[i] == '0':
                    hist[i + 1] = 0
                else:
                    hist[i + 1] += 1
            stack = [0]
            for i in range(1, n + 2):
                while hist[i] < hist[stack[-1]]:
                    height = hist[stack.pop()]
                    width = i - stack[-1] - 1
                    mx = max(mx, min(width, height)**2)
                stack.append(i)
        return mx
