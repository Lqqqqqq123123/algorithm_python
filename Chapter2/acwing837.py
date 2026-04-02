import sys
sys.setrecursionlimit(100000)


# 定义并查集
p, size = [], []


def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]


def merge(x, y):
    px, py = find(x), find(y)
    if px == py:return 
    size[py] += size[px]
    p[px] = py


n, m = map(int, input().split())

for i in range(m):
    lines = input().split()
    if lines[0] == 'C':
        merge(int(lines[1]), int(lines[2]))
    elif lines[0] == 'Q1':
        A = find(int(lines[1]))
        B = find(int(lines[2]))
        print('Yes' if A == B else 'No')
    elif lines[0] == 'Q2':
        print(size[find(int(lines[1]))])
