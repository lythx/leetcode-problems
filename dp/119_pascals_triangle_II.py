from typing import List

class Solution:
    def getRow(self, n: int) -> List[int]:
        ans = [1]
        for k in range(1, (n + 2) // 2):
            ans.append(ans[-1] * (n - k + 1) // k)
        if n % 2 == 0:
            return ans + ans[:-1][::-1]
        return ans + ans[::-1]
