import heapq


class MedianFinder:

    def __init__(self):
        self.n = 0
        self.heap_min = []
        self.heap_max = []

    def addNum(self, num: int) -> None:
        if self.n == 0:
            self.heap_max.append(-num)
        elif self.n == 1:
            if num >= -self.heap_max[0]:
                self.heap_min.append(num)
            else:
                self.heap_min.append(-self.heap_max[0])
                self.heap_max[0] = -num
        elif self.n % 2 == 0:
            if num > self.heap_min[0]:
                val = heapq.heappushpop(self.heap_min, num)
                heapq.heappush(self.heap_max, -val)
            else:
                heapq.heappush(self.heap_max, -num)
        else:
            if num > self.heap_min[0]:
                heapq.heappush(self.heap_min, num)
            else:
                val = -heapq.heappushpop(self.heap_max, -num)
                heapq.heappush(self.heap_min, val)
        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 0:
            return (self.heap_min[0] - self.heap_max[0]) / 2
        return -self.heap_max[0]
