import bisect
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people.sort()
        mask = [i for i in range(n)]
        new_mask = [i for i in range(n)]
        ans: list[(int, int)] = [None] * n
        for i in range(n):
            if i > 0 and people[i][0] > people[i - 1][0]:
                print('NEWMASK')
                mask = new_mask.copy()
            print(ans, people[i])
            w, k = people[i]
            ind = bisect.bisect_left(mask, k)
            print(ind, mask)
            ans[ind] = people[i]
            for j in range(ind, n):
                new_mask[j] -= 1
        print(ans)
        return ans


Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])