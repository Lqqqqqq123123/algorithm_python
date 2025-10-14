# 滑动窗口
from collections import deque # python中的队列（双向队列）
import sys
input = sys.stdin.readline
write = sys.stdout.write

res1, res2 = [], [] # 存储最大值和最小值
n, k = map(int, input().split())

arr = list(map(int, input().split()))

# 单调队列
q1, q2 = deque(), deque()

for i in range(n):
    # 剔除过期元素
    while q1 and i - q1[0] >= k: q1.popleft()
    while q2 and i - q2[0] >= k: q2.popleft()

    # 剔除队列中所有小于当前元素的元素
    while q1 and arr[q1[-1]] <= arr[i]: q1.pop()

    # 剔除队列中所有大于当前元素的元素
    while q2 and arr[q2[-1]] >= arr[i]: q2.pop()


    # 添加当前元素
    q1.append(i)
    q2.append(i)
    # 看看是否已经形成窗口
    if i >= k - 1: res1.append(arr[q1[0]]); res2.append(arr[q2[0]])

write(' '.join(map(str, res2)) + '\n')
write(' '.join(map(str, res1)) + '\n')