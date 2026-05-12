from typing import List, Optional

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(x, y):
            grid[x][y] = 'x'
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != '1':
                    continue
                dfs(nx, ny)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1

        return res
