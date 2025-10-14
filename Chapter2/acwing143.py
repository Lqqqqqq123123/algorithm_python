import sys


# 快读快些

input = sys.stdin.readline
prt = sys.stdout.write

n = int(input())
arr = list(map(int, input().split()))

# 字典树把每个数从高到低存下来

son = [[-1] * 2 for _ in range(n * 31)]
idx = 0

def insert(x:int):
    global idx
    p = 0
    for i in range(30, -1, -1):
        u = (x >> i) & 1
        if son[p][u] == -1:
            idx += 1
            son[p][u] = idx
        p = son[p][u]

def query(x:int):
    p = 0
    t = 0
    for i in range(30, -1, -1):
        u = (x >> i) & 1
        if son[p][1 - u] != -1:
            t = (t << 1) | 1
            p = son[p][1 - u]
        else:
            t = (t << 1)
            p = son[p][u]
    return t

res = 0

for i in range(n):
    insert(arr[i])

for i in range(n):
    res = max(res, query(arr[i]))

print(res)