class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: (-x[0], x[1]))
        count = 0
        smallest = second = 1000000000000
        for start, end in intervals:
            contains_smallest = end >= smallest
            contains_second = end >= second
            if contains_second and contains_smallest:
                continue
            if contains_smallest:
                second = smallest
                smallest = start
                count += 1
            else:
                second = start + 1
                smallest = start
                count += 2
        return count