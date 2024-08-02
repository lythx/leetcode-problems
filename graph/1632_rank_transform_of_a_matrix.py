from typing import List
from math import inf

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        row_rank = [0] * m
        col_rank = [0] * n
        row_max = [-inf] * m
        col_max = [-inf] * n

        d = dict()
        for i in range(m):
            for j in range(n):
                x = matrix[i][j]
                if x not in d:
                    d[x] = [(i, j)]
                else:
                    d[x].append((i, j))

        answer = [[0] * n for _ in range(m)]
        for val in sorted(d.keys()):
            rank = 0
            for row, col in d[val]:
                if row_max[row] == val:
                    rank = max(rank, row_rank[row])
                else:
                    rank = max(rank, row_rank[row] + 1)

                if col_max[col] == val:
                    rank = max(rank, col_rank[col])
                else:
                    rank = max(rank, col_rank[col] + 1)

            for row, col in d[val]:
                row_rank[row] = col_rank[col] = rank
                row_max[row] = col_max[col] = val
                answer[row][col] = rank

        return answer

Solution().matrixRankTransform([[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]])
