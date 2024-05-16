from typing import List


class Solution:
    def catMouseGame(self, G: List[List[int]]) -> int:
        n = len(G)
        # state[move][mouse_position][cat_position]
        # 0 - mouse move, 1 - cat move
        # 0 - draw, 1 - mouse wins, 2 - cat wins, 3 - impossible
        state = [[[0] * n for _ in range(n)] for _ in range(2)]
        for u in range(n):
            state[0][0][u] = 1
            state[1][0][u] = 1
            state[0][u][0] = 3
            state[1][u][0] = 3
            state[0][u][u] = 2
            state[1][u][u] = 2
        while True:
            changed = False
            for u in range(n):
                for v in range(n):

                    if state[0][u][v] == 0:
                        win = False
                        draw = False
                        for w in G[u]:
                            if state[1][w][v] == 1:
                                win = True
                                break
                            elif state[1][w][v] == 0:
                                draw = True
                        if win:
                            changed = True
                            state[0][u][v] = 1
                        elif not draw:
                            changed = True
                            state[0][u][v] = 2

                    if state[1][u][v] == 0:
                        win = False
                        draw = False
                        for w in G[v]:
                            if state[0][u][w] == 2:
                                win = True
                                break
                            elif state[0][u][w] == 0:
                                draw = True
                        if win:
                            changed = True
                            state[1][u][v] = 2
                        elif not draw:
                            changed = True
                            state[1][u][v] = 1
            if state[0][1][2] != 0 or (not changed):
                return state[0][1][2]
