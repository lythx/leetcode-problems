from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, left: List[int], right: List[int]) -> bool:
        if sum([0 if x == -1 else 1 for x in left]) + \
                sum([0 if x == -1 else 1 for x in right]) != n - 1:
            return False
        has_parent = [False] * n
        for u in range(n):
            if left[u] != -1:
                if has_parent[left[u]]:
                    return False
                has_parent[left[u]] = True
            if right[u] != -1:
                if has_parent[right[u]]:
                    return False
                has_parent[right[u]] = True
        if has_parent.count(False) != 1:
            return False
        root = has_parent.index(False)
        visited = [False] * n
        print(root)

        def dfs(u):
            if left[u] != -1:
                visited[left[u]] = True
                dfs(left[u])
            if right[u] != -1:
                visited[right[u]] = True
                dfs(right[u])

        visited[root] = True
        dfs(root)
        return not (False in visited)
