from typing import List, Optional
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh = 0 # 新鲜的橘子数量
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # 队列
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))

                elif grid[i][j] == 1:
                    fresh += 1


        # 去腐烂新鲜橘子
        res = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()

                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    fresh -= 1
                    q.append((nx, ny))
                    if fresh == 0:
                        return res

            res += 1
        return -1 if fresh != 0 else res

