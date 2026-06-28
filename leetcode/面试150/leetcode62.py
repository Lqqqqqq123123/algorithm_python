from typing import List
class Solution:
    def uniquePaths(self, n: int, m: int) -> int:

        f = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    f[i][j] = 1
                else:
                    if i > 0:
                        f[i][j] += f[i - 1][j]
                    if j > 0:
                        f[i][j] += f[i][j - 1]


        return f[n - 1][m - 1]

