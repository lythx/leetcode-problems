from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        n2 = 1 << n
        visited = [False] * n2
        visited[0] = True
        powers_of_2 = set()
        p = 1
        while p < n2:
            powers_of_2.add(p)
            p <<= 1

        def dfs(x, visit_count):
            print(x, (x << 0), (x << 1), x << 5, visit_count, visited)
            if visit_count == n2:
                if x in powers_of_2:
                    return [x]
                return False
            i = 0
            while i < n:
                if (x >> i) % 2 == 0:
                    y = x + (1 << i)
                else:
                    y = x - (1 << i)
                if y >= n2:
                    break
                if not visited[y]:
                    visited[y] = True
                    ans = dfs(y, visit_count + 1)
                    if ans:
                        ans.append(x)
                        return ans
                    visited[y] = False
                i += 1
            return False

        ans = dfs(0, 1)
        ans.reverse()
        return ans

Solution().grayCode(5)
