from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [True] * n

        def dfs(i):
            if i == n:
                return True
            if memo[i] == False:
                return False
            for w in wordDict:
                if w == s[i:i + len(w)] and dfs(i + len(w)):
                    return True
            memo[i] = False
            return False

        return dfs(0)

