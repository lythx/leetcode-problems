import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        n = len(courses)
        courses.sort(key=lambda x: x[1])
        heap = []
        dursum = 0
        for i in range(n):
            dur, last = courses[i]
            if dur > last:
                continue
            if last >= dur + dursum:
                heapq.heappush(heap, -dur)
                dursum += dur
            elif -heap[0] > dur:
                val = -heapq.heapreplace(heap, -dur)
                dursum += dur - val
        return len(heap)
