from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for offset in range(n // 2):
            for i in range(offset, n - offset - 1):
                a = matrix[offset][i]
                b = matrix[i][n - offset - 1]
                c = matrix[n - offset - 1][n - i - 1]
                d = matrix[n - i - 1][offset]
                matrix[offset][i] = d
                matrix[i][n - offset - 1] = a
                matrix[n - offset - 1][n - i - 1] = b
                matrix[n - i - 1][offset] = c
