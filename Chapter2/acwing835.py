# Python 版本 Tire树

import sys
input = sys.stdin.readline
prt = sys.stdout.write

N = int(1e5 + 10)

# 用数组模拟 Tire 树
son = [[0] * 26 for _ in range(N)]
cnt, idx = [0] * N, 0

def insert(s : str):
    global idx
    p = 0
    for c in s:
        u = ord(c) - ord('a')
        if son[p][u] == 0:
            idx += 1
            son[p][u] = idx
        p = son[p][u]
    
    cnt[p] += 1

def query(s : str) -> int:
    p = 0
    for c in s:
        u = ord(c) - ord('a')
        if son[p][u] == 0: return 0
        p = son[p][u]
    return cnt[p]


n = int(input())

for i in range(n):
    op, s = input().split()
    if op == "I":
        insert(s)
    else:
        print(query(s))

        