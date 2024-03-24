import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mx = max(nums)
        mn = min(nums)
        counts = [[0, i] for i in range(mx - mn + 1)]
        for x in nums:
            counts[x - mn][0] -= 1
        heapq.heapify(counts)
        ans = [0] * k
        for i in range(k):
            ans[i] = heapq.heappop(counts)[1] + mn
        return ans


Solution().topKFrequent([1,1,1,2,2,3], 2)

