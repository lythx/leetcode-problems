from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        n = len(dictionary)
        k = len(s)
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            j = 0
            flag = True
            for i in range(len(word)):
                while j < k and word[i] != s[j]:
                    j += 1
                if j == k:
                    flag = False
                    break
                j += 1
            if flag:
                return word
        return ""
