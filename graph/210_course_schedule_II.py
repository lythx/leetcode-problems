from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
        visited = [False] * numCourses
        cur_visited = [False] * numCourses
        stack = []
        found_cycle = False

        def topo_sort(v):
            nonlocal found_cycle
            if cur_visited[v]:
                found_cycle = True
                return
            if visited[v]:
                return
            visited[v] = True
            cur_visited[v] = True
            for i in adj[v]:
                if found_cycle:
                    return
                topo_sort(i)
            cur_visited[v] = False
            stack.append(v)

        for i in range(numCourses):
            if not visited[i]:
                topo_sort(i)
            if found_cycle:
                return []
        return stack
