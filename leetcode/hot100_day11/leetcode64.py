from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        f = [[float('inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    f[i][j] = grid[i][j]
                else:
                    if i - 1 >= 0:
                        f[i][j] = min(f[i][j], f[i - 1][j] + grid[i][j])
                    if j - 1 >= 0:
                        f[i][j] = min(f[i][j], f[i][j - 1] + grid[i][j])

        return f[n - 1][m - 1]

