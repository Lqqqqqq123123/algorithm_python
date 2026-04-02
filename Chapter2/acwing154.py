# 滑动窗口 
import sys
from collections import deque

r = sys.stdin.readline
w = sys.stdout.write

q1, q2 = deque(), deque()
n, k = map(int, r().split())
res1, res2 = [], []
a = list(map(int, r().split()))


for i in range(n):
    # 删除过期的元素
    while q1 and i - q1[0] + 1 > k: q1.popleft()
    while q2 and i - q2[0] + 1 > k: q2.popleft()

    # 删除没用的元素
    # 求最小值
    while q1 and a[q1[-1]] >= a[i]: q1.pop()
    # 求最大值
    while q2 and a[q2[-1]] <= a[i]: q2.pop()
    q1.append(i)
    q2.append(i)

    if i >= k - 1:
        res1.append(a[q1[0]])
        res2.append(a[q2[0]])

w(" ".join(map(str, res1)) + "\n")
w(" ".join(map(str, res2)))