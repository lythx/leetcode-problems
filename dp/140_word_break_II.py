from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        ans = []
        memo = [True] * n

        def dfs(i, words):
            if i == n:
                ans.append(words[:-1])
                return True
            if not memo[i]:
                return False
            flag = False
            for w in wordDict:
                if w == s[i:i + len(w)] and dfs(i + len(w), words + w + " "):
                    flag = True
            if not flag:
                memo[i] = False
            return flag

        dfs(0, "")
        return ans
