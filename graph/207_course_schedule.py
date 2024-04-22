from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
        visited = [False] * numCourses
        cur_visited = [False] * numCourses

        def dfs(v):
            if cur_visited[v]:
                return True
            if visited[v]:
                return False
            cur_visited[v] = True
            visited[v] = True
            for u in adj[v]:
                if dfs(u):
                    return True
            cur_visited[v] = False
            return False

        for i in range(numCourses):
            if visited[i]:
                continue
            if dfs(i):
                return False
        return True
