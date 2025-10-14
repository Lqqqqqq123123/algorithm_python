# 食物链：带权并查集维护三倍关系  x -> y -> z -> x

import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
prt = sys.stdout.write

N = int(1e5 + 10)

p, d = [i for i in range(N)], [0] * N  # d[i] 表示 i 到其根节点的距离

def find(x):
    if p[x] != x:
        f = find(p[x])
        d[x] += d[p[x]]
        p[x] = f
    return p[x]


n, k = map(int, input().split())
res = 0

for i in range(k):
    op, x, y = map(int, input().split())
    px, py = find(x), find(y)

    if x > n or y > n:
        res += 1
        continue

    if op == 1:
        # x 和 y 是同类
        # 如何它两不再一个集合，就维护它两的关系，负责就去判断是否矛盾
        if px != py:
            p[px] = py
            d[px] = d[y] - d[x]
        else:
            if (d[x] - d[y]) % 3 != 0:
                res += 1
    else:
        # x 吃 y
        if x == y:
            res += 1
            continue
        if px != py:
            p[px] = py
            d[px] = d[y] - d[x] + 1
        else:
            if (d[x] - d[y] - 1) % 3 != 0:
                res += 1

print(res)