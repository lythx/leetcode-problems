from typing import List
from pyvis.network import Network

class Solution:
    def eventualSafeNodes(self, G: List[List[int]]) -> List[int]:
        n = len(G)
        # 0 - not checked, 1 - unsafe, 2 - safe
        visited = [0] * n

        def dfs(u):
            print(u, G[u])
            print(list(enumerate(visited)))
            for v in G[u]:
                if visited[v] == 1:
                    return 1
                visited[v] = 1
                visited[v] = dfs(v)
                if visited[v] == 1:
                    return 1
            visited[u] = 2
            return 2

        for u in range(n):
            if not visited[u]:
                visited[u] = 1
                visited[u] = dfs(u)

        ans = []
        for u in range(n):
            if visited[u] == 2:
                ans.append(u)
        return ans

# G = [[1,3,4],[0,8],[2,5,6,9],[8],[7,9],[1,6,7],[7,8],[],[9],[9]]
# E = []
# for u in range(len(G)):
#     for v in G[u]:
#         E.append([u, v])
# net = Network(notebook = True, cdn_resources = "remote",
#               bgcolor = "#222222",
#               font_color = "white",
#               height = "750px",
#               width = "100%",
#               directed=True
#               )
# net.add_nodes([i for i in range(len(G))])
# net.add_edges(E)
# net.show("graph.html")