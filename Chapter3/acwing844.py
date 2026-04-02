import sys
from collections import deque # 队列


# 快读快些
input = sys.stdin.readline
w = sys.stdout.write

n, m = map(int, input().split())
directions= [(0, 1), (0, -1), (1, 0), (-1, 0)]
g, d = [[]] * n, [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    g[i] = list(map(int, input().split()))


def bfs():
    # 初始化队列 + 源点入队
    q = deque([(0, 0)])
    d[0][0] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0 and d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))

                # 找到终点
                if nx == n - 1 and ny == m - 1:
                    return d[nx][ny]
                
    
    return d[n - 1][m - 1]



bfs()
w(str(d[n - 1][m - 1]))