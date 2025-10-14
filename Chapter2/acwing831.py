# kmp python实现

import sys
# 快读快些
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
p = input().strip()
m = int(input())
s = input().strip()

ne = [0] * (n + 1)
res = []

# 先做一遍kmp，获得ne数组
j = 0
for i in range(2, n + 1):
    while j and p[j] != p[i - 1]: j = ne[j]
    if p[j] == p[i - 1]: j += 1
    ne[i] = j

j = 0
# kmp匹配算法
for i in range(m):
    while j and s[i] != p[j]: j = ne[j]
    if s[i] == p[j]: j += 1
    if j == n:
        res.append(i - n + 1)
        j = ne[j]


write(' '.join(map(str, res)))