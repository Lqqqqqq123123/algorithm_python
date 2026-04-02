# 邻接矩阵存图

n, m = map(int, input().split())

g = [[] * n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    g[x][y] = g[y][x] = 1


# 邻接表存图
g = [[] for _ in range(n + 1)]

def add(a, b):
    g[a].append(b); g[b].append(a)

def addwithweight(a, b, w):
    g[a].append([b, w]); g[b].append([a, w])


# 字典实现
from collections import defaultdict
g = defaultdict(dict)
