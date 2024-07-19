from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        palindromes = [[[] for _ in range(n)] for _ in range(n)]
        for center in range(n):
            i = 0
            while center - i >= 0 and center + i < n and s[center - i] == s[center + i]:
                palindromes[center - i][center + i].append(s[center - i:center + i + 1])
                i += 1

            i = 0
            while center - i >= 0 and center + 1 + i < n and s[center - i] == s[center + 1 + i]:
                palindromes[center - i][center + 1 + i].append(s[center - i:center + 1 + i + 1])
                i += 1

        def dfs(i, parts, ans):
            if i == n:
                ans.append(parts)
                return
            for j in range(n):
                for p in palindromes[i][j]:
                    dfs(i + len(p), parts + [p], ans)

        ans = []
        dfs(0, [], ans)
        return ans




