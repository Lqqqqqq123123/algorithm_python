# 模拟哈希表
# 方式一：拉链法

import sys
input = sys.stdin.readline
prt = sys.stdout.write

# 多重链表
N = int(1e5 + 10)

h, e, ne, idx = [-1] * N, [0] * N, [0] * N, 0

def add(x:int):
    global idx
    u = (x % N + N) % N
    e[idx] = x; ne[idx] = h[u]; h[u] = idx; idx += 1

def find(x: int):
    u = (x % N + N) % N   # 计算桶号
    i = h[u]              # i 是桶的第一个节点索引
    while i != -1:        # 从链表头遍历
        if e[i] == x:
            return True
        i = ne[i]
    return False
      


n = int(input())

for i in range(n):
    op, x = input().split()
    if op == "I":
        add(int(x))
    else:
        if find(int(x)):
            prt("Yes\n")
        else:
            prt("No\n")