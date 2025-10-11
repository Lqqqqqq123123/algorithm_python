import sys
from collections import deque
input = sys.stdin.readline

q = deque()

m = int(input())

for i in range(m):
    lines = input().split()
    op = lines[0]

    if op == 'push':
        # push 操作
        q.append(int(lines[1]))
    elif op == 'pop':
        # pop 操作
        q.popleft()
    elif op == 'empty':
        # empty 操作
        print("YES" if len(q) == 0 else "NO")
    else:
        # query 操作
        print(q[0])

