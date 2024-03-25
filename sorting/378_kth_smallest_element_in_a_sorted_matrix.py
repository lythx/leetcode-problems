import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(x, 0, i) for i, x in enumerate(matrix[0])]
        heapq.heapify(heap)
        for i in range(k - 1):
            val, row, col = heap[0]
            if row == n - 1:
                heapq.heappop(heap)
            else:
                heapq.heapreplace(heap, (matrix[row + 1][col], row + 1, col))
        return heap[0][0]
