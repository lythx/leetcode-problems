from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        max_w = max(envelopes, key=lambda x: x[0])[0]
        min_w = min(envelopes, key=lambda x: x[0])[0]
        max_h = max(envelopes, key=lambda x: x[1])[1]
        min_h = min(envelopes, key=lambda x: x[1])[1]
        w_count = [0] * (max_w - min_w + 1)
        h_count = [0] * (max_h - min_h + 1)
        for e in envelopes:
            w_count[e[0] - min_w] += 1
            h_count[e[1] - min_h] += 1
        for i in range(max_w - min_w - 1, -1, -1):
            w_count[i] += w_count[i + 1]
        for i in range(max_h - min_h - 1, -1 ,-1):
            h_count[i] += h_count[i + 1]
        mn = n + 1
        for e in envelopes:
            s = w_count[e[0] - min_w] + h_count[e[1] - min_h]
            if s < mn:
                mn = s
        return n - mn + 1
