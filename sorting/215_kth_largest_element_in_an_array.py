import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for i in range(k, n):
            heapq.heappushpop(heap, nums[i])
        return heap[0]



Solution().findKthLargest([3,2,1,5,6,4], 2)