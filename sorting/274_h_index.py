from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts_len = max(citations) + 1
        counts = [0] * counts_len
        for c in citations:
            counts[c] += 1
        for i in range(counts_len - 2, -1, -1):
            counts[i] += counts[i + 1]
        print(counts)
        for i in range(counts_len - 1, -1, -1):
            if counts[i] >= i:
                return i
        return 0

print(Solution().hIndex([1,3,1]))
