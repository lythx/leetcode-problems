class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        vis = set()
        start = "0" * (n - 1)
        ans = []

        def dfs(u):
            nonlocal ans
            for i in range(k):
                v = u + str(i)
                if v not in vis:
                    vis.add(v)
                    dfs(v[1:])
                    ans.append(str(i))

        dfs(start)
        return "".join(ans) + start