from typing import List, Optional

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, gd, dg, col = [], [False] * (2 * n), [False] * (2 * n), [False] * n
        g = [['.'] * n for _ in range(n)]

        def dfs(row, k):
            if row == n:
                if k == n:
                    temp = []
                    for i in range(n):
                        temp.append(''.join(g[i]))
                    res.append(temp)
                return


            for j in range(n):
                if not col[j] and not gd[row + j] and not dg[row - j + n]:
                    g[row][j] = 'Q'
                    col[j] = gd[row + j] = dg[row - j + n] = True
                    dfs(row + 1, k + 1)
                    g[row][j] = '.'
                    col[j] = gd[row + j] = dg[row - j + n] = False

        dfs(0, 0)
        return res