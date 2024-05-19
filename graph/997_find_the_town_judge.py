from typing import List


class Solution:
    def findJudge(self, n: int, E: List[List[int]]) -> int:
        if n == 1 and len(E) == 0:
            return 1
        trusts_someone = set()
        trusted_by = {}
        for a, b in E:
            trusts_someone.add(a)
            if b in trusted_by:
                trusted_by[b] += 1
            else:
                trusted_by[b] = 1
        for a, t in trusted_by.items():
            if t == n - 1 and a not in trusts_someone:
                return a
        return -1

